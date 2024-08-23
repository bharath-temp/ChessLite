# allows python interpreter to defer evaluation of Bishop type to the future
from __future__ import annotations

from typing import override

from src.pieces.chesspiece import Piece
from src.utils.colors import PieceColor


class Bishop(Piece):
    """Represents a Bishop chess piece.

    Attributes:
        _color (PieceColor): The color of the piece.
        _current_row (int): The current row position of the piece.
        _current_col (int): The current column position of the piece.
    """
    def __init__(self, color: PieceColor, current_row: int, current_col: int):
        """Initializes a Bishop piece with the specified color and position.

        Args:
            color (PieceColor): The color of the piece.
            current_row (int): The initial row position of the piece.
            current_col (int): The initial column position of the piece.
        """
        super().__init__(color, current_row, current_col)

    @staticmethod
    def create_bishop(color: PieceColor, current_row: int,
                      current_col: int) -> Bishop:
        """Factory method to create a Bishop piece.

        Args:
            color (PieceColor): The color of the piece.
            current_row (int): The row position to place the Bishop.
            current_col (int): The column position to place the Bishop.

        Returns:
            Bishop: A new Bishop instance.
        """
        return Bishop(color, current_row, current_col)

    def _is_valid_bishop_move(self, dest_row: int, dest_col: int) -> bool:
        """Checks if the move to the destination is valid for the Bishop.

        Bishops can only move diagonally, which means the row and column
        changes must be equal.

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

        # Bishops can only move diagonally
        return (row_change == col_change)
