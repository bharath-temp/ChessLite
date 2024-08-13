import pytest

from src.pieces.king import King
from src.utils.colors import PieceColor


def test_king_factory_method():
    """Test the create_king factory method."""
    king = King.create_king(PieceColor.BLACK, 0, 4)
    assert isinstance(king, King)
    assert king.get_color() == PieceColor.BLACK
    assert king.get_row() == 0
    assert king.get_column() == 4


@pytest.fixture
def king_test():
    return King.create_king(PieceColor.WHITE, 1, 1)


def test_king_initialization(king_test):
    """Test that the King class is initialized with the correct
       color, row and col.
    """
    assert isinstance(king_test, King)
    assert king_test._color == PieceColor.WHITE
    assert king_test._current_row == 1
    assert king_test._current_col == 1


def test_king_get_color_method(king_test):
    """Test the get_color method of the King class."""
    assert king_test.get_color() == PieceColor.WHITE
    assert king_test.get_color() != PieceColor.BLACK


def test_king_get_row_method(king_test):
    """Test the get_row method of the King class."""
    assert king_test.get_row() == 1


def test_king_get_col_method(king_test):
    """Test the get_col method of the King class."""
    assert king_test.get_column() == 1
