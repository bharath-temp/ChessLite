import pytest

from src.pieces.bishop import Bishop
from src.utils.colors import PieceColor


def test_bishop_factory_method():
    """Test the create_bishop factory method."""
    bishop = Bishop.create_bishop(PieceColor.BLACK, 0, 4)
    assert isinstance(bishop, Bishop)
    assert bishop.color == PieceColor.BLACK
    assert bishop.row == 0
    assert bishop.column == 4


@pytest.fixture
def bishop_test():
    return Bishop.create_bishop(PieceColor.WHITE, 1, 1)


def test_bishop_initialization(bishop_test):
    """Test that the bishop class is initialized with the correct
       color, row and col.
    """
    assert isinstance(bishop_test, Bishop)
    assert bishop_test._color == PieceColor.WHITE
    assert bishop_test._current_row == 1
    assert bishop_test._current_col == 1


def test_bishop_get_color_method(bishop_test):
    """Test the get_color method of the bishop class."""
    assert bishop_test.color == PieceColor.WHITE
    assert bishop_test.color != PieceColor.BLACK


def test_bishop_get_row_method(bishop_test):
    """Test the get_row method of the bishop class."""
    assert bishop_test.row == 1


def test_bishop_get_col_method(bishop_test):
    """Test the get_col method of the Bishop class."""
    assert bishop_test.column == 1


def test_bishop_set_row_method(bishop_test):
    """Test the set_row method of the Bishop class."""
    bishop_test.row = 2
    assert bishop_test.row == 2


def test_bishop_set_col_method(bishop_test):
    """Test the set_column method of the Bishop class."""
    bishop_test.column = 3
    assert bishop_test.column == 3
