import json

from src.pieces import Bishop, King, Knight, Pawn, \
                       Piece, PieceFactory, Queen, Rook
from src.piece_manager import PieceManager
from src.players import Player, AIPlayer, HumanPlayer
from src.rules import CheckedHelperRule, FundPieceMoveRule, PathClearRule, \
                      PathClearHelperRule, SameColorRule, \
                      SelfCheckRule, CheckMatedRule, CapturePieceRule
from src.utils import PieceColor, PieceType, PlayerType


BOARD_SIZE = 8


class GameController():
    def __init__(self, piece_manager: PieceManager, player_one: Player,
                 player_two: Player):
        self.__piece_manager = piece_manager
        self.__player_one = player_one
        self.__player_two = player_two

        self.__checked_helper_rule = CheckedHelperRule(
            self.__piece_manager
        )
        self.__path_clear_helper_rule = PathClearHelperRule(
                self.__piece_manager
        )

        same_color_rule = SameColorRule(self.__piece_manager)
        fund_move_rule = FundPieceMoveRule(self.__piece_manager)
        path_clear_rule = PathClearRule(self.__piece_manager,
                                        self.__path_clear_helper_rule)
        capture_piece_rule = CapturePieceRule(self.__piece_manager)
        self_check_rule = SelfCheckRule(self.__piece_manager,
                                        self.__checked_helper_rule)

        self.__rules_chain = same_color_rule
        self.__rules_chain.set_next(fund_move_rule) \
                          .set_next(path_clear_rule) \
                          .set_next(capture_piece_rule) \
                          .set_next(self_check_rule)

        self.__check_mated_rule = CheckMatedRule(self.__piece_manager,
                                                 self.__checked_helper_rule,
                                                 self.__rules_chain)

        self.__current_player = self.__player_one
        self.__game_over = False

    def get_current_player(self):
        return self.__current_player

    def __switch_turn(self) -> None:
        if self.__current_player == self.__player_one:
            self.__current_player = self.__player_two
        else:
            self.__current_player = self.__player_one

    def handle_player_input(self, row: int, col: int, target_row: int,
                            target_col: int) -> None:
        print(f"func: get_player_input {self.__current_player.color}")
        piece = self.__piece_manager.get_piece_at(row, col)
        if self.validate_player_move(row, col, target_row, target_col):
            capture_piece = self.__piece_manager.get_piece_at(target_row,
                                                              target_col)
            if capture_piece is not None:
                self.__piece_manager.remove_piece_at(target_row, target_col)

            self.__piece_manager.place_piece_at(piece, target_row,
                                                target_col)
            self.__switch_turn()

    def validate_player_move(self, row: int, col: int, target_row: int,
                             target_col: int) -> bool:
        print(f"func: validate_player_move {self.__current_player.color}")
        piece = self.__piece_manager.get_piece_at(row, col)
        if piece is None:
            print("No piece there")
            return False

        piece_repr = f"{piece.color} {piece.__class__.__name__}"

        if not self.__rules_chain.validate(piece, self.__current_player,
                                           target_row, target_col):
            print(f"{piece_repr} move invalid")
            return False

        return True

    def is_checkmate(self) -> bool:
        if self.__check_mated_rule.validate(self.__current_player):
            print(f"Checkmate! {self.__current_player.color.name} loses.")
            self.__game_over = True
            return True

        return False

    def forfeit(self) -> None:
        print(f"{self.__current_player.color} player has forfeited the game.")
        if self.__current_player == self.__player_one:
            print(f"{self.__player_two.color} player wins!")
        else:
            print(f"{self.__player_one.color} player wins!")

        self.__game_over = True

    def is_game_over(self) -> bool:
        return self.__game_over

    def serialize_board_state(self):
        piece_state_serial = self.__piece_manager.serialize_piece_state()

        player_info = {
            "player_name": self.__current_player.name,
            "player_color": self.__current_player.color.name
        }

        board_state = {
            "board": json.loads(piece_state_serial),
            "player": player_info
        }

        return board_state
