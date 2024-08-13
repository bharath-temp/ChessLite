# allows python interpreter to defer evaluation of Queen type to the future
from __future__ import annotations

from typing import override

from src.pieces.chesspiece import Piece
from src.utils.colors import PieceColor


class Queen(Piece):
    def __init__(self, color: PieceColor, current_row: int, current_col: int):
        super().__init__(color, current_row, current_col)

    # Factory method to create Queen piece
    @staticmethod
    def create_queen(color: PieceColor, current_row: int,
                     current_col: int) -> Queen:
        return Queen(color, current_row, current_col)

    @override
    def get_color(self) -> PieceColor:
        return self._color

    @override
    def get_row(self) -> int:
        return self._current_row

    @override
    def get_column(self) -> int:
        return self._current_col

    def _is_valid_queen_move(self, dest_row: int, dest_col: int) -> bool:
        if not super()._is_valid_move(dest_row, dest_col):
            return False

        curr_row = self.get_row()
        curr_col = self.get_column()

        row_change = abs(curr_row - dest_row)
        col_change = abs(curr_col - dest_col)

        return (row_change <= 1 and col_change <= 1)
