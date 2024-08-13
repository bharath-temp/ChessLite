# allows python interpreter to defer evaluation of King type to the future
from __future__ import annotations

from typing import override

from src.pieces.chesspiece import Piece
from src.utils.colors import PieceColor


class King(Piece):
    """
    Represents a King chess piece.

    Attributes:
        _color (PieceColor): The color of the piece.
        _current_row (int): The current row position of the piece.
        _current_col (int): The current column position of the piece.
        _moved (bool): Tracks if the King has moved.
    """

    def __init__(self, color: PieceColor, current_row: int, current_col: int):
        """
        Initializes a King piece with the specified color and position.

        Args:
            color (PieceColor): The color of the piece.
            current_row (int): The initial row position of the piece.
            current_col (int): The initial column position of the piece.
        """
        super().__init__(color, current_row, current_col)
        self._moved = False

    @staticmethod
    def create_king(color: PieceColor, current_row: int,
                    current_col: int) -> King:
        """
        Factory method to create a King piece.

        Args:
            color (PieceColor): The color of the piece.
            current_row (int): The row position to place the King.
            current_col (int): The column position to place the King.

        Returns:
            King: A new King instance.
        """
        return King(color, current_row, current_col)

    @override
    def get_color(self) -> PieceColor:
        """See base class."""
        return self._color

    @override
    def get_row(self) -> int:
        """See base class."""
        return self._current_row

    @override
    def get_column(self) -> int:
        """See base class."""
        return self._current_col

    def get_moved(self) -> bool:
        """Returns True if King has moved"""
        return self._moved

    @override
    def set_row(self, dest_row: int) -> None:
        """See base class."""
        self._current_row = dest_row

    @override
    def set_column(self, dest_col: int) -> None:
        """See base class."""
        self._current_col = dest_col

    def set_moved(self) -> None:
        """Marks the King as having moved."""
        self._moved = True

    def _is_valid_king_move(self, dest_row: int, dest_col: int) -> bool:
        """
        Checks if the move to the destination is valid for the King.

        Args:
            dest_row (int): The destination row position.
            dest_col (int): The destination column position.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        if not super()._is_valid_move(dest_row, dest_col):
            return False

        curr_row = self.get_row()
        curr_col = self.get_column()

        row_change = abs(curr_row - dest_row)
        col_change = abs(curr_col - dest_col)

        # Kings can only move 1 square in any direction
        return (row_change <= 1 and col_change <= 1)
