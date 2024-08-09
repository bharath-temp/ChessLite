from abc import ABC, abstractmethod
from src.utils.colors import PieceColor

class Piece(ABC):
    def __init__(self, color: PieceColor, current_row: int, current_col: int) -> None:
        self._color = color
        self._current_row = current_row
        self._current_col = current_col

    @abstractmethod
    def get_color(self) -> PieceColor:
        pass

    @abstractmethod
    def get_row(self) -> int:
        pass

    @abstractmethod
    def get_column(self) -> int:
        pass

    def in_bounds_check(self, row: int, col: int) -> bool:
        return ((0 <= row < 8) and (0 <= col <8))

    @abstractmethod
    def valid_move(self, dest_row: int, dest_col: int) -> bool:
        if not self.in_bounds_check(dest_row, dest_col) or \
            ((self._current_row == dest_row) and (self._current_col == dest_col)):
            return False

        return True