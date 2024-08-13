import pytest

from src.pieces.queen import Queen
from src.utils.colors import PieceColor


def test_queen_factory_method():
    """Test the create_queen factory method."""
    queen = Queen.create_queen(PieceColor.BLACK, 0, 4)
    assert isinstance(queen, Queen)
    assert queen.get_color() == PieceColor.BLACK
    assert queen.get_row() == 0
    assert queen.get_column() == 4


@pytest.fixture
def queen_test():
    return Queen.create_queen(PieceColor.WHITE, 1, 1)


def test_queen_initialization(queen_test):
    """Test that the queen class is initialized with the correct
       color, row and col.
    """
    assert isinstance(queen_test, Queen)
    assert queen_test._color == PieceColor.WHITE
    assert queen_test._current_row == 1
    assert queen_test._current_col == 1


def test_queen_get_color_method(queen_test):
    """Test the get_color method of the queen class."""
    assert queen_test.get_color() == PieceColor.WHITE
    assert queen_test.get_color() != PieceColor.BLACK


def test_queen_get_row_method(queen_test):
    """Test the get_row method of the queen class."""
    assert queen_test.get_row() == 1


def test_queen_get_col_method(queen_test):
    """Test the get_col method of the queen class."""
    assert queen_test.get_column() == 1
