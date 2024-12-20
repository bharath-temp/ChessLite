from abc import ABC, abstractmethod

from src.utils.colors import PieceColor
from src.utils.piece_type import PieceType


class Piece(ABC):
    """Abstract base class for a chess piece.

    Attributes:
        _color (PieceColor): The color of the piece.
        _current_row (int): The current row position of the piece.
        _current_col (int): The current column position of the piece.
    """

    def __init__(self, color: PieceColor, piece_type: PieceType,
                 current_row: int, current_col: int) -> None:
        """Initializes a chess piece with the specified color and position.

        Args:
            color (PieceColor): The color of the piece.
            current_row (int): The initial row position of the piece.
            current_col (int): The initial column position of the piece.
        """
        self._color = color
        self._piece_type = piece_type
        self._current_row = current_row
        self._current_col = current_col

    @property
    def color(self) -> PieceColor:
        """The color of the piece.

        Returns:
            PieceColor: The color of the piece.
        """
        return self._color

    @property
    def piece_type(self) -> PieceType:
        """The type of the piece.

        Returns:
            PieceType: The type of the piece.
        """
        return self._piece_type

    @property
    def row(self) -> int:
        """The current row of the piece.

        Returns:
            int: The current row of the piece.
        """
        return self._current_row

    @row.setter
    def row(self, dest_row: int) -> None:
        """Updates the current row of the piece.

        Args:
            dest_row (int): The new row position for the piece.
        """
        self._current_row = dest_row

    @property
    def column(self) -> int:
        """The current column of the piece.

        Returns:
            int: The current column of the piece.
        """
        return self._current_col

    @column.setter
    def column(self, dest_col: int) -> None:
        """Updates the current column of the piece.

        Args:
            dest_col (int): The new column position for the piece.
        """
        self._current_col = dest_col

    def _on_position_changed(self) -> None:
        """Hook method called when the piece's position changes.

           Intended to be overridden by subclasses that need
           to perform actions when the position is updated.
        """
        pass

    def set_position(self, dest_row: int, dest_col: int) -> None:
        """Updates the position of the piece, invokes the on position changed
           method.

        Args:
            dest_row (int): The new row position.
            dest_col (int): The new column position.
        """
        self.row = dest_row
        self.col = dest_col
        self._on_position_changed()

    def _in_bounds_check(self, row: int, col: int) -> bool:
        """Checks if the given position is within the bounds of the chessboard.

        Args:
            row (int): The row position to check.
            col (int): The column position to check.

        Returns:
            bool: True if the position is within bounds, False otherwise.
        """
        return ((0 <= row < 8) and (0 <= col < 8))

    def _is_valid_move(self, dest_row: int, dest_col: int) -> bool:
        """Checks if the move to the destination is valid.

        Args:
            dest_row (int): The destination row position.
            dest_col (int): The destination column position.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        '''
        All pieces must stay in bounds on the board and can't move to the
        same location
        '''
        if (
            not self._in_bounds_check(dest_row, dest_col)
            or (
                self.row == dest_row
                and self.column == dest_col
            )
        ):
            return False

        return True

    @abstractmethod
    def _validate_piece_move(self, dest_row: int, dest_col: int) -> bool:
        """Validates the piece-specific movement rules.

        Example: A Knight moves in an "L" shape, which means two squares in
        one direction and one square in the perpendicular direction.

        Args:
            dest_row (int): The destination row position.
            dest_col (int): The destination column position.

        Returns:
            bool: True if the move is valid according to the piece's rules,
            False otherwise.
        """
        pass
