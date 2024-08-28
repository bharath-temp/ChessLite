from src.pieces import Bishop, King, Knight, Pawn, \
                       Piece, PieceFactory, Queen, Rook
from src.utils import PieceColor, PieceType


BOARD_SIZE = 8
CELL_WIDTH = 5


class GameBoard():
    def __init__(self):
        self.board = [[None for _ in range(BOARD_SIZE)]
                      for _ in range(BOARD_SIZE)]
        self.white_pieces = []
        self.black_pieces = []

    def display_board(self):
        for row in self.board:
            display_row = []
            for cell in row:
                if cell is None:
                    display_row.append(' ' * CELL_WIDTH)
                else:
                    centered_cell = str(cell).center(CELL_WIDTH)
                    display_row.append(centered_cell)
            print(f"{"|".join(display_row)}")
            print(f"{"-" * (CELL_WIDTH * BOARD_SIZE + (BOARD_SIZE - 1))}")
        print(f"\n")

    def update_board(self):
        self.board = [[None for _ in range(BOARD_SIZE)]
                      for _ in range(BOARD_SIZE)]

        for piece in self.white_pieces:
            piece_symbol = f"W{piece.__class__.__name__[:2]}"
            self.board[piece.row][piece.column] = piece_symbol

        for piece in self.black_pieces:
            piece_symbol = f"B{piece.__class__.__name__[:2]}"
            self.board[piece.row][piece.column] = piece_symbol

    def populate_board_pawns(self, color: PieceColor):
        if color == PieceColor.WHITE:
            row = 6
            piece_list = self.white_pieces
        else:
            row = 1
            piece_list = self.black_pieces

        for col in range(BOARD_SIZE):
            new_pawn = PieceFactory.create_piece(PieceType.PAWN, color,
                                                 row, col)
            piece_list.append(new_pawn)

    def populate_board_major_pieces(self, color: PieceColor):
        if color == PieceColor.WHITE:
            row = 7
            piece_list = self.white_pieces
        else:
            row = 0
            piece_list = self.black_pieces

        major_pieces = [
            (PieceType.ROOK, 0), (PieceType.KNIGHT, 1), (PieceType.BISHOP, 2),
            (PieceType.QUEEN, 3), (PieceType.KING, 4), (PieceType.BISHOP, 5),
            (PieceType.KNIGHT, 6), (PieceType.ROOK, 7)
        ]

        for piece_type, col in major_pieces:
            new_piece = PieceFactory.create_piece(piece_type, color, row, col)
            piece_list.append(new_piece)


# Test the GameBoard class
def test_game_board():
    board = GameBoard()
    board.populate_board_pawns(PieceColor.WHITE)
    board.populate_board_pawns(PieceColor.BLACK)
    board.populate_board_major_pieces(PieceColor.WHITE)
    board.populate_board_major_pieces(PieceColor.BLACK)
    board.update_board()
    board.display_board()


test_game_board()
