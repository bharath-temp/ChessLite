import unittest

from src.pieces.king import King
from src.utils.colors import Piece_Color


class TestKingPiece(unittest.TestCase):
    def test_king_initialization(self):
        """Test that the King class is initialized with the correct color."""
        king = King()
        self.assertIsInstance(king, King)
        self.assertEqual(king.color, Piece_Color.WHITE)

    def test_king_my_color_method(self):
        """Test the my_color method of the King class."""
        king = King()
        self.assertEqual(king.my_color(), Piece_Color.WHITE)


if __name__ == '__main__':
    unittest.main()
