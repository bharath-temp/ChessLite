# allows python interpreter to defer evaluation of Pawn type to the future
from __future__ import annotations

from typing import override

from src.pieces.chesspiece import Piece
from src.pieces.mixins.moved_piece_mixin import MovedPieceMixin
from src.pieces.piece_factory import PieceFactory
from src.utils.colors import PieceColor
from src.utils.piece_type import PieceType


@PieceFactory.register_piece(PieceType.PAWN)
class Pawn(Piece, MovedPieceMixin):
    """Represents a Pawn chess piece.

    Attributes:
        _color (PieceColor): The color of the piece.
        _current_row (int): The current row position of the piece.
        _current_col (int): The current column position of the piece.
        _moved (bool): Tracks if the Rook has moved (inherited from
                       MovedPieceMixin).
    """

    def __init__(self, color: PieceColor, current_row: int, current_col: int):
        """Initializes a Pawn piece with the specified color and position.

        Args:
            color (PieceColor): The color of the piece.
            current_row (int): The initial row position of the piece.
            current_col (int): The initial column position of the piece.
        """
        super().__init__(color, current_row, current_col)
        self._moved = False

    def _can_promote(self) -> bool:
        """Checks if the Pawn can be promoted.

        A Pawn can be promoted if it reaches the opposite end of the board.

        Returns:
            bool: True if the Pawn can be promoted, False otherwise.
        """
        color = self.color
        curr_row = self.row

        if (color == PieceColor.WHITE) and (curr_row == 0):
            return True
        if (color == PieceColor.BLACK) and (curr_row == 7):
            return True

        return False

    @override
    def _validate_piece_move(self, dest_row: int, dest_col: int) -> bool:
        """Overrides piece-specific move validation for the Pawn.

        Pawns move forward one square, or two squares on their first move.
        They capture diagonally.

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

        # Pawns can only move forward in the direction respective to color
        if ((self.color == PieceColor.WHITE) and (dest_row < self.row) or
                (self.color == PieceColor.BLACK) and (dest_row > self.row)):
            return False

        # Pawns can move forward 1 square, standard move
        if (row_change == 1) and (col_change == 0):
            return True

        # Pawns can move forward two squares if it hasn't moved yet.
        if (row_change == 2) and (col_change == 0) and (self.moved is False):
            return True

        # Pawns can move diagonally to take enemy piece or via en pessant
        if (row_change == 1) and (col_change == 1):
            return True

        return False
