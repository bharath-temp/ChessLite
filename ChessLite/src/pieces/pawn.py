# allows python interpreter to defer evaluation of Pawn type to the future
from __future__ import annotations

from typing import override

from src.pieces.chesspiece import Piece
from src.utils.colors import PieceColor


class Pawn(Piece):
    def __init__(self, color: PieceColor, current_row: int, current_col: int):
        super().__init__(color, current_row, current_col)
        self._moved = False

    # Factory method to create Pawn piece
    @staticmethod
    def create_pawn(color: PieceColor, current_row: int,
                    current_col: int) -> Pawn:
        return Pawn(color, current_row, current_col)

    @override
    def get_color(self) -> PieceColor:
        return self._color

    @override
    def get_row(self) -> int:
        return self._current_row

    @override
    def get_column(self) -> int:
        return self._current_col

    def get_moved(self) -> bool:
        return self._moved

    def set_moved(self) -> None:
        self._moved = True

        return None

    def _can_promote(self) -> bool:
        color = self.get_color()
        curr_row = self.get_row()

        if (color == PieceColor.WHITE) and (curr_row == 7):
            return True
        if (color == PieceColor.BLACK) and (curr_row == 0):
            return True

        return False

    def _is_valid_pawn_move(self, dest_row: int, dest_col: int) -> bool:
        if not super()._is_valid_move(dest_row, dest_col):
            return False

        curr_row = self.get_row()
        curr_col = self.get_column()
        color = self.get_color()
        moved = self.get_moved()
        row_change = abs(curr_row - dest_row)
        col_change = abs(curr_col - dest_col)

        if (color == PieceColor.WHITE) and (dest_row - curr_row < 1):
            return False
        if (color == PieceColor.BLACK) and (dest_row - curr_row > -1):
            return False

        if (row_change == 1) and (col_change == 0):
            return True

        if (row_change == 2) and (col_change == 0) and (moved is False):
            return True

        if (row_change == 1) and (col_change == 1):
            return True

        return False
