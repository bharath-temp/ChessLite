from src.pieces.chesspiece import ChessPiece
from src.utils.colors import ObjColor

class King(ChessPiece):
    def __init__(self, piece_color: ObjColor):
        super().__init__(piece_color)

    def my_color(self) -> ObjColor:
        return self.color