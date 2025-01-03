# allows python interpreter to defer evaluation of King type to the future
from __future__ import annotations

from typing import override

from src.pieces.chesspiece import Piece
from src.pieces.move_status import MoveStatus
from src.pieces.piece_factory import PieceFactory
from src.utils.colors import PieceColor
from src.utils.piece_type import PieceType


@PieceFactory.register_piece(PieceType.KING)
class King(Piece):
    """Represents a King chess piece.

    Attributes:
        _color (PieceColor): The color of the piece.
        _current_row (int): The current row position of the piece.
        _current_col (int): The current column position of the piece.
        _moved (bool): Tracks if the Rook has moved (inherited from
                       MoveStatus).
    """

    def __init__(self, color: PieceColor, current_row: int, current_col: int):
        """Initializes a King piece with the specified color and position.

        Args:
            color (PieceColor): The color of the piece.
            current_row (int): The initial row position of the piece.
            current_col (int): The initial column position of the piece.
        """
        super().__init__(color, PieceType.KING, current_row, current_col)
        self._move_status = MoveStatus()

    @override
    def _on_position_changed(self) -> None:
        """Overrides move checking function, ensuring that
           piece moves are recorded.
        """
        self._move_status.moved = True

    @override
    def _validate_piece_move(self, dest_row: int, dest_col: int) -> bool:
        """Overrides piece-specific move validation for the King.

        Kings move one square in any direction.

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

        # Kings can only move 1 square in any direction
        return (row_change <= 1 and col_change <= 1)
