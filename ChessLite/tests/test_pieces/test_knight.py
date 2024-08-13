import pytest

from src.pieces.knight import Knight
from src.utils.colors import PieceColor


def test_knight_factory_method():
    """Test the create_knight factory method."""
    knight = Knight.create_knight(PieceColor.BLACK, 0, 4)
    assert isinstance(knight, Knight)
    assert knight.get_color() == PieceColor.BLACK
    assert knight.get_row() == 0
    assert knight.get_column() == 4


@pytest.fixture
def knight_test():
    return Knight.create_knight(PieceColor.WHITE, 1, 1)


def test_knight_initialization(knight_test):
    """Test that the knight class is initialized with the correct
       color, row and col.
    """
    assert isinstance(knight_test, Knight)
    assert knight_test._color == PieceColor.WHITE
    assert knight_test._current_row == 1
    assert knight_test._current_col == 1


def test_knight_get_color_method(knight_test):
    """Test the get_color method of the Knight class."""
    assert knight_test.get_color() == PieceColor.WHITE
    assert knight_test.get_color() != PieceColor.BLACK


def test_knight_get_row_method(knight_test):
    """Test the get_row method of the Knight class."""
    assert knight_test.get_row() == 1


def test_knight_get_col_method(knight_test):
    """Test the get_col method of the Knight class."""
    assert knight_test.get_column() == 1


def test_knight_set_row_method(knight_test):
    """Test the set_row method of the Knight class."""
    knight_test.set_row(2)
    assert knight_test.get_row() == 2


def test_knight_set_col_method(knight_test):
    """Test the set_column method of the knight class."""
    knight_test.set_column(3)
    assert knight_test.get_column() == 3
