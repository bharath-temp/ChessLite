from src.pieces.chesspiece import Piece
from src.utils.piece_type import PieceType
from src.utils.colors import PieceColor


class PieceFactory():
    """Factory class for creating and registering chess pieces.

    This class manages the registration and creation of chess piece instances
    based on the provided piece type. Pieces are registered using the
    `register_piece` class method and can be created using the `create_piece`
    static method.
    """

    __piece_registry = {}

    @classmethod
    def register_piece(cls, piece_type: PieceType):
        """Decorator to register a chess piece class with the factory.

        This method returns a decorator that registers the provided piece class
        with the factory under the specified piece type.

        Args:
            piece_type (PieceType): The type of chess piece to register.

        Returns:
            function: A decorator function that registers the piece class.
        """
        def wrapper(piece_class: Piece):
            if piece_type not in cls.__piece_registry:
                cls.__piece_registry[piece_type] = piece_class

            return piece_class

        return wrapper

    @staticmethod
    def create_piece(piece_type: PieceType, color: PieceColor, row: int,
                     col: int):
        """Creates an instance of a registered chess piece.

        This method retrieves the class associated with the specified piece
        type from the registry and creates an instance of it using the
        provided color, row, and column.

        Args:
            piece_type (PieceType): The type of chess piece to create.
            color (Color): The color of the chess piece.
            row (int): The starting row position of the chess piece.
            col (int): The starting column position of the chess piece.

        Returns:
            Piece: An instance of the requested chess piece.

        Raises:
            ValueError: If the piece type is not registered.
        """
        piece_class = PieceFactory.__piece_registry.get(piece_type)
        if not piece_class:
            raise ValueError(f"Piece type {piece_type} is not registered.")

        return piece_class(color, row, col)
