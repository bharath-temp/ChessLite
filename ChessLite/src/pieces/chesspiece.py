from abc import ABC, abstractmethod

from src.utils.colors import PieceColor


class Piece(ABC):
    """
    Abstract base class for a chess piece.

    Attributes:
        _color (PieceColor): The color of the piece.
        _current_row (int): The current row position of the piece.
        _current_col (int): The current column position of the piece.
    """

    def __init__(self, color: PieceColor, current_row: int,
                 current_col: int) -> None:
        """
        Initializes a chess piece with the specified color and position.

        Args:
            color (PieceColor): The color of the piece.
            current_row (int): The initial row position of the piece.
            current_col (int): The initial column position of the piece.
        """
        self._color = color
        self._current_row = current_row
        self._current_col = current_col

    @abstractmethod
    def get_color(self) -> PieceColor:
        """Returns the color of the Piece."""
        pass

    @abstractmethod
    def get_row(self) -> int:
        """Returns the current row of the Piece."""
        pass

    @abstractmethod
    def get_column(self) -> int:
        """Returns the current column of the Piece."""
        pass

    @abstractmethod
    def set_row(self, dest_row: int) -> None:
        """Sets the current row of the piece."""
        pass

    @abstractmethod
    def set_column(self, dest_col: int) -> None:
        """Sets the current column of the piece."""
        pass

    def __in_bounds_check(self, row: int, col: int) -> bool:
        """
        Checks if the given position is within the bounds of the chessboard.

        Args:
            row (int): The row position to check.
            col (int): The column position to check.

        Returns:
            bool: True if the position is within bounds, False otherwise.
        """
        return ((0 <= row < 8) and (0 <= col < 8))

    def _is_valid_move(self, dest_row: int, dest_col: int) -> bool:
        """
        Checks if the move to the destination is valid.

        Args:
            dest_row (int): The destination row position.
            dest_col (int): The destination column position.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        '''
        All pieces must stay in bounds on the boardand can't move to the
        same location
        '''
        if (
            not self._in_bounds_check(dest_row, dest_col)
            or (
                self._current_row == dest_row
                and self._current_col == dest_col
            )
        ):
            return False

        return True
