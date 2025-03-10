from src.pieces import Bishop, King, Knight, Pawn, \
                       Piece, PieceFactory, Queen, Rook
from src.piece_manager import PieceManager
from src.utils import PieceColor, PieceType, PlayerType


BOARD_SIZE = 8
CELL_WIDTH = 5


class GameBoard():
    def __init__(self, piece_manager: PieceManager):
        self.board = [[None for _ in range(BOARD_SIZE)]
                      for _ in range(BOARD_SIZE)]
        self.__piece_manager = piece_manager

    def display_board(self) -> None:
        # Display column numbers on top
        column_numbers = " " + " ".join(
            str(i).center(CELL_WIDTH) for i in range(BOARD_SIZE)
        )
        print(column_numbers)

        for row_index, row in enumerate(self.board):
            display_row = []
            for cell in row:
                if cell is None:
                    display_row.append(' ' * CELL_WIDTH)
                else:
                    centered_cell = str(cell).center(CELL_WIDTH)
                    display_row.append(centered_cell)
            print(f"{row_index} |" + "|".join(display_row) + f"| {row_index}")
            print(f"  {'-' * (CELL_WIDTH * BOARD_SIZE + (BOARD_SIZE - 1))}")

        # Display column numbers on the bottom
        print(column_numbers)
        print("\n")

    def update_board(self) -> None:
        self.board = [[None for _ in range(BOARD_SIZE)]
                      for _ in range(BOARD_SIZE)]

        for piece in self.__piece_manager.pieces:
            piece_color = "W" if piece.color == PieceColor.WHITE else "B"
            piece_symbol = f"{piece_color}{piece.__class__.__name__[:2]}"
            self.board[piece.row][piece.column] = piece_symbol
