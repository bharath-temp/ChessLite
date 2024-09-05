import pytest

from src.pieces import Queen, PieceFactory
from src.utils import PieceColor, PieceType


def test_queen_factory_method():
    """Test the create_queen factory method."""
    queen = PieceFactory.create_piece(PieceType.QUEEN, PieceColor.BLACK, 0, 4)
    assert isinstance(queen, Queen)
    assert queen.color == PieceColor.BLACK
    assert queen.row == 0
    assert queen.column == 4


@pytest.fixture
def queen_test():
    return PieceFactory.create_piece(PieceType.QUEEN, PieceColor.WHITE, 1, 1)


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
    assert queen_test.color == PieceColor.WHITE
    assert queen_test.color != PieceColor.BLACK


def test_queen_get_row_method(queen_test):
    """Test the get_row method of the queen class."""
    assert queen_test.row == 1


def test_queen_get_col_method(queen_test):
    """Test the get_col method of the queen class."""
    assert queen_test.column == 1


def test_queen_set_row_method(queen_test):
    """Test the set_row method of the queen class."""
    queen_test.row = 2
    assert queen_test.row == 2


def test_queen_set_col_method(queen_test):
    """Test the set_column method of the queen class."""
    queen_test.column = 3
    assert queen_test.column == 3
