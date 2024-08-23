# allows python interpreter to defer evaluation of Knight type to the future
from __future__ import annotations

from typing import override

from src.pieces.chesspiece import Piece
from src.utils.colors import PieceColor


class Knight(Piece):
    """Represents a Knight chess piece.

    Attributes:
        _color (PieceColor): The color of the piece.
        _current_row (int): The current row position of the piece.
        _current_col (int): The current column position of the piece.
    """

    def __init__(self, color: PieceColor, current_row: int, current_col: int):
        """Initializes a Knight piece with the specified color and position.

        Args:
            color (PieceColor): The color of the piece.
            current_row (int): The initial row position of the piece.
            current_col (int): The initial column position of the piece.
        """
        super().__init__(color, current_row, current_col)

    @staticmethod
    def create_knight(color: PieceColor, current_row: int,
                      current_col: int) -> Knight:
        """Factory method to create a Knight piece.

        Args:
            color (PieceColor): The color of the piece.
            current_row (int): The row position to place the Knight.
            current_col (int): The column position to place the Knight.

        Returns:
            Knight: A new Knight instance.
        """
        return Knight(color, current_row, current_col)

    def _is_valid_knight_move(self, dest_row: int, dest_col: int) -> bool:
        """Checks if the move to the destination is valid for the Knight.

        Knights move in an "L" shape: two squares in one direction and
        one square in the perpendicular direction, or one square in one
        direction and two squares in the perpendicular direction.

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

        # Knights can move 2 and 1 vertically or horizontally
        if (row_change == 2 and col_change == 1):
            return True
        elif (row_change == 1 and col_change == 2):
            return True
        else:
            return False
