# allows python interpreter to defer evaluation of King type to the future
from __future__ import annotations

from src.pieces.piece import Piece
from src.utils.colors import PieceColor

class King(Piece):
    def __init__(self, color: PieceColor, current_row: int, current_col: int):
        super().__init__(color, current_row, current_col)

    # Factory method to create king piece
    @staticmethod
    def create_king(color: PieceColor, current_row: int, current_col: int) -> King:
        return King(color, current_row, current_col)

    def get_color(self) -> PieceColor:
        return self._color

    def get_row(self) -> int:
        return self._current_row

    def get_column(self) -> int:
        return self._current_col

    def valid_move(self, dest_row: int, dest_col: int) -> bool:
        if not super().valid_move(dest_row, dest_col):
            return False

        curr_row = self.get_row()
        curr_col = self.get_column()

        row_change = abs(curr_row - dest_row)
        col_change = abs(curr_col - dest_col)
        
        return (row_change <= 1 and col_change <= 1)