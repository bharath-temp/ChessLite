from abc import ABC, abstractmethod
from src.utils.colors import ObjColor

class ChessPiece(ABC):
    def __init__(self, color: ObjColor) -> None:
        self.color = color

    @abstractmethod
    def my_color(self):
        pass