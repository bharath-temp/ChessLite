from src.pieces import Bishop, King, Knight, Pawn, \
                       Piece, PieceFactory, Queen, Rook
from src.piece_manager import PieceManager
from src.players import Player, AIPlayer, HumanPlayer
from src.utils import PieceColor, PieceType, PlayerType


BOARD_SIZE = 8


class GameController():
    def __init__(self, piece_manager: PieceManager, player_one: Player,
                 player_two: Player):
        self.__piece_manager = piece_manager
        self.__player_one = player_one
        self.__player_two = player_two
        self.__current_player = player_one
        self.__game_over = False

    def __switch_turn(self) -> None:
        if self.__current_player == self.__player_one:
            self.__current_player = self.__player_two
        else:
            self.__current_player = self.__player_one

    def get_player_input(self, row: int, col: int, target_row: int,
                         target_col: int) -> None:
        print(f"func: get_player_input {self.__current_player.color}")
        piece = self.__piece_manager.get_piece_at(row, col)
        if self.validate_player_move(row, col, target_row, target_col):
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

        # can't move different color piece
        if piece.color is not self.__current_player.color:
            print(f"{piece_repr} can't move, not same color")
            return False

        # fundamental piece movement error
        if not piece._validate_piece_move(target_row, target_col):
            print(f"{piece_repr} piece can't move that way")
            return False

        # piece can't move there, path is blocked
        if not self.__is_path_clear(piece, target_row, target_col):
            print(f"{piece_repr} piece is blocked")
            return False

        # piece movement will cause self check
        if self.__would_cause_check(piece, target_row, target_col):
            print(f"{piece_repr} piece will cause self check")
            return False

        return True

    def __is_path_clear(self, piece: Piece, target_row: int,
                        target_col: int) -> bool:
        print(f"func: __is_path_clear {self.__current_player.color}")
        # Check the target square for an opponent piece
        # (which would be a valid capture)
        target_piece = self.__piece_manager.get_piece_at(target_row,
                                                         target_col)
        if target_piece and target_piece.color == piece.color:
            return False

        if isinstance(piece, Knight):
            return True

        if target_row > piece.row:
            row_step = 1
        elif target_row < piece.row:
            row_step = -1
        else:
            row_step = 0

        if target_col > piece.column:
            col_step = 1
        elif target_col < piece.column:
            col_step = -1
        else:
            col_step = 0

        print(
            f"out while {piece}:{piece.color} orig from"
            f"{piece.row}-{piece.column} to {target_row}-{target_col}"
        )

        row_offset = piece.row + row_step
        col_offset = piece.column + col_step

        while row_offset != target_row or col_offset != target_col:
            print(
                f"out while {piece}:{piece.color} orig from"
                f"{piece.row}-{piece.column} to {target_row}-{target_col}"
            )
            if self.__piece_manager.get_piece_at(row_offset, col_offset):
                return False

            row_offset += row_step
            col_offset += col_step

        return True

    def __is_in_check(self) -> bool:
        print(f"func: __is_in_check {self.__current_player.color}")
        king = self.__piece_manager.get_king(self.__current_player.color)
        king_row = king.row
        king_col = king.column

        for piece in self.__piece_manager.pieces:
            if piece.color != self.__current_player.color:
                if piece._validate_piece_move(king_row, king_col) and \
                   self.__is_path_clear(piece, king_row, king_col):
                    print(f"{piece}-{piece.color} has you in check!")
                    return True

        print(f"func: out of __is_in_check {self.__current_player.color}")
        return False

    def is_checkmate(self) -> bool:
        if self.__is_in_check() is False:
            return False

        for piece in self.__piece_manager.pieces:
            if piece.color == self.__current_player.color:
                continue

            orig_row = piece.row
            orig_col = piece.column

            for row in range(BOARD_SIZE):
                for col in range(BOARD_SIZE):
                    if self.__is_valid_and_clear(orig_row, orig_col, row,
                                                 col, piece):
                        if not self.__would_cause_check(piece, row, col):
                            return False

        print(f"Checkmate! {self.__current_player.color.name} loses.")
        self.__game_over = True
        return True

    def __is_valid_and_clear(self, orig_row, orig_col, row, col, piece):
        return self.validate_player_move(orig_row, orig_col, row, col) and \
               self.__is_path_clear(piece, row, col)

    def __would_cause_check(self, piece: Piece, target_row: int,
                            target_col: int) -> bool:
        print(f"func: __would_cause_check {self.__current_player.color}")
        orig_row = piece.row
        orig_col = piece.column

        self.__piece_manager.place_piece_at(piece, target_row, target_col)
        is_checked = self.__is_in_check()
        self.__piece_manager.place_piece_at(piece, orig_row, orig_col)

        return is_checked

    def forfeit(self) -> None:
        print(f"{self.__current_player.color} player has forfeited the game.")
        if self.__current_player == self.__player_one:
            print(f"{self.__player_two.color} player wins!")
        else:
            print(f"{self.__player_one.color} player wins!")

        self.__game_over = True

    def is_game_over(self) -> bool:
        return self.__game_over
