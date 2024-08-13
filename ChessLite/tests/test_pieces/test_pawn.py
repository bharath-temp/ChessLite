import pytest

from src.pieces.pawn import Pawn
from src.utils.colors import PieceColor


def test_pawn_factory_method():
    """Test the create_pawn factory method."""
    pawn = Pawn.create_pawn(PieceColor.BLACK, 0, 4)
    assert isinstance(pawn, Pawn)
    assert pawn.get_color() == PieceColor.BLACK
    assert pawn.get_row() == 0
    assert pawn.get_column() == 4


@pytest.fixture
def pawn_test():
    return Pawn.create_pawn(PieceColor.WHITE, 1, 1)


def test_pawn_initialization(pawn_test):
    """Test that the pawn class is initialized with the correct
       color, row and col.
    """
    assert isinstance(pawn_test, Pawn)
    assert pawn_test._color == PieceColor.WHITE
    assert pawn_test._current_row == 1
    assert pawn_test._current_col == 1


def test_pawn_get_color_method(pawn_test):
    """Test the get_color method of the pawn class."""
    assert pawn_test.get_color() == PieceColor.WHITE
    assert pawn_test.get_color() != PieceColor.BLACK


def test_pawn_get_row_method(pawn_test):
    """Test the get_row method of the pawn class."""
    assert pawn_test.get_row() == 1


def test_pawn_get_col_method(pawn_test):
    """Test the get_col method of the pawn class."""
    assert pawn_test.get_column() == 1


def test_pawn_set_row_method(pawn_test):
    """Test the set_row method of the Pawn class."""
    pawn_test.set_row(2)
    assert pawn_test.get_row() == 2


def test_pawn_set_col_method(pawn_test):
    """Test the set_column method of the Pawn class."""
    pawn_test.set_column(3)
    assert pawn_test.get_column() == 3


def test_pawn_set_moved_method(pawn_test):
    """Test the set_moved method of the Pawn class."""
    assert not pawn_test.get_moved()  # Initially should be False
    pawn_test.set_moved()
    assert pawn_test.get_moved()  # After setting should be True
