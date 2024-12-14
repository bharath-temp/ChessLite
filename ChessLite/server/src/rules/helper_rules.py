from typing import override

from src.pieces import Piece
from src.players import Player
from src.piece_manager import PieceManager
from src.rules.rule import Rule
from src.pieces import Bishop, King, Knight, Pawn, \
                       Piece, PieceFactory, Queen, Rook
from src.utils.piece_type import PieceType


class CheckedHelperRule(Rule):
    @override
    def validate(self, player: Player) -> bool:
        king = self._piece_manager.get_king(player.color)
        king_row = king.row
        king_col = king.column

        opp_pieces = self._piece_manager.get_opponent_pieces(player.color)

        path_clear_helper = PathClearHelperRule(self._piece_manager)

        for piece in opp_pieces:
            if isinstance(piece, Pawn):
                row_diff = abs(piece.row - king_row)
                col_diff = abs(piece.column - king_col)

                if row_diff == 1 and col_diff == 1:
                    print(f"Pawn at {piece.row}-{piece.column}"
                          f"is putting you in check")
                    return True
            else:
                if piece._validate_piece_move(king_row, king_col) and \
                   path_clear_helper.validate(piece, player, king_row,
                                              king_col):
                    target_piece = piece
                    print(f"{target_piece}-{target_piece.color}"
                          f"{target_piece.row} {target_piece.column}"
                          f"put you in check")
                    print(f"You're in check")
                    return True

        return False


class PathClearHelperRule(Rule):
    @override
    def validate(self, piece: Piece, player: Player, target_row: int,
                 target_col: int) -> bool:
        if self.__target_square_occupied(piece, target_row,
                                         target_col) is False:
            print(f"Piece is occupied by same color at {target_row},"
                  f"{target_col}")
            return False

        if piece.piece_type is PieceType.KNIGHT:
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

        row_offset = piece.row + row_step
        col_offset = piece.column + col_step

        while row_offset != target_row or col_offset != target_col:
            if self._piece_manager.get_piece_at(row_offset, col_offset):
                print(f"Piece is obstructed")
                return False

            row_offset += row_step
            col_offset += col_step

        return True

    def __target_square_occupied(self, piece: Piece, target_row: int,
                                 target_col: int) -> bool:
        target_piece = self._piece_manager.get_piece_at(target_row,
                                                        target_col)
        if target_piece and target_piece.color == piece.color:
            print(f"theres a piece there {target_piece.color}"
                  f"{target_piece.row}"
                  f"{target_piece.column}")
            return False

        return True
