from src.pieces import Bishop, King, Knight, Pawn, \
                       Piece, PieceFactory, Queen, Rook
from src.utils import PieceColor, PieceType


BOARD_SIZE = 8


class PieceManager():
    def __init__(self):
        self.pieces = []
        self.__initialize_pawns()
        self.__initialize_major_pieces()

    def __initialize_pawns(self) -> None:
        row_color_settings = [(6, PieceColor.WHITE), (1, PieceColor.BLACK)]

        for (row, color) in row_color_settings:
            for col in range(BOARD_SIZE):
                new_pawn = PieceFactory.create_piece(PieceType.PAWN, color,
                                                     row, col)
                self.pieces.append(new_pawn)

    def __initialize_major_pieces(self) -> None:
        row_color_settings = [(7, PieceColor.WHITE), (0, PieceColor.BLACK)]

        major_pieces = [
            (PieceType.ROOK, 0), (PieceType.KNIGHT, 1), (PieceType.BISHOP, 2),
            (PieceType.QUEEN, 3), (PieceType.KING, 4), (PieceType.BISHOP, 5),
            (PieceType.KNIGHT, 6), (PieceType.ROOK, 7)
        ]

        for (row, color) in row_color_settings:
            for piece_type, col in major_pieces:
                new_piece = PieceFactory.create_piece(piece_type, color,
                                                      row, col)
                self.pieces.append(new_piece)

    def get_piece_at(self, row: int, col: int) -> Piece:
        for piece in self.pieces:
            if piece.row == row and piece.column == col:
                return piece

        return None

    def get_king(self, color: PieceColor) -> Piece:
        for piece in self.pieces:
            if isinstance(piece, King) and piece.color == color:
                return piece

    def place_piece_at(self, piece: Piece, target_row: int,
                       target_col: int) -> None:
        piece.row = target_row
        piece.column = target_col
