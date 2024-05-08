from src.pieces.chesspiece import ChessPiece
from src.utils.colors import ObjColor

class King(ChessPiece):
    def __init__(self):
        super().__init__(ObjColor.WHITE)

    def my_color(self) -> ObjColor:
        return self.color