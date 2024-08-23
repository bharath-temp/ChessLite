# allows python interpreter to defer evaluation of Queen type to the future
from __future__ import annotations

from typing import override

from src.pieces.chesspiece import Piece
from src.utils.colors import PieceColor


class Queen(Piece):
    """Represents a Queen chess piece.

    Attributes:
        _color (PieceColor): The color of the piece.
        _current_row (int): The current row position of the piece.
        _current_col (int): The current column position of the piece.
    """

    def __init__(self, color: PieceColor, current_row: int, current_col: int):
        """Initializes a Queen piece with the specified color and position.

        Args:
            color (PieceColor): The color of the piece.
            current_row (int): The initial row position of the piece.
            current_col (int): The initial column position of the piece.
        """
        super().__init__(color, current_row, current_col)

    @staticmethod
    def create_queen(color: PieceColor, current_row: int,
                     current_col: int) -> Queen:
        """Factory method to create a Queen piece.

        Args:
            color (PieceColor): The color of the piece.
            current_row (int): The row position to place the Queen.
            current_col (int): The column position to place the Queen.

        Returns:
            Queen: A new Queen instance.
        """
        return Queen(color, current_row, current_col)

    def _is_valid_queen_move(self, dest_row: int, dest_col: int) -> bool:
        """Checks if the move to the destination is valid for the Queen.

        The Queen can move diagonally, vertically, or horizontally. The move
        is valid if the row and column changes are either equal (diagonal)
        or one of them is zero (vertical or horizontal).

        Args:
            dest_row (int): The destination row position.
            dest_col (int): The destination column position.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        if not super()._is_valid_move(dest_row, dest_col):
            return False

        row_change = abs(self.row - dest_row)
        col_change = abs(self.col - dest_col)

        # Queens can move diagonally or vertically or horizontally
        if (row_change == col_change):
            return True
        elif (row_change > 0 and col_change == 0):
            return True
        elif (col_change > 0 and row_change == 0):
            return True
        else:
            return False
