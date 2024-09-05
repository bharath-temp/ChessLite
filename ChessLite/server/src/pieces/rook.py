# allows python interpreter to defer evaluation of Rook type to the future
from __future__ import annotations

from typing import override

from src.pieces.chesspiece import Piece
from src.pieces.mixins.moved_piece_mixin import MovedPieceMixin
from src.pieces.piece_factory import PieceFactory
from src.utils.colors import PieceColor
from src.utils.piece_type import PieceType


@PieceFactory.register_piece(PieceType.ROOK)
class Rook(Piece, MovedPieceMixin):
    """Represents a Rook chess piece.

    Attributes:
        _color (PieceColor): The color of the piece.
        _current_row (int): The current row position of the piece.
        _current_col (int): The current column position of the piece.
        _moved (bool): Tracks if the Rook has moved (inherited from
                       MovedPieceMixin).
    """

    def __init__(self, color: PieceColor, current_row: int, current_col: int):
        """Initializes a Rook piece with the specified color and position.

        Args:
            color (PieceColor): The color of the piece.
            current_row (int): The initial row position of the piece.
            current_col (int): The initial column position of the piece.
        """
        super().__init__(color, PieceType.ROOK, current_row, current_col)
        self._moved = False

    @override
    def _validate_piece_move(self, dest_row: int, dest_col: int) -> bool:
        """Overrides piece-specific move validation for the Rook.

        The Rook moves vertically or horizontally.

        Args:
            dest_row (int): The destination row position.
            dest_col (int): The destination column position.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        if not super()._is_valid_move(dest_row, dest_col):
            return False

        row_change = abs(self.row - dest_row)
        col_change = abs(self.column - dest_col)

        # Rooks can only move in 2 direction vertically or horizontally
        if (row_change > 0 and col_change == 0):
            return True
        elif (col_change > 0 and row_change == 0):
            return True
        else:
            return False