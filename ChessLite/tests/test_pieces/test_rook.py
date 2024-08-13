import pytest

from src.pieces.rook import Rook
from src.utils.colors import PieceColor


def test_rook_factory_method():
    """Test the create_rook factory method."""
    rook = Rook.create_rook(PieceColor.BLACK, 0, 4)
    assert isinstance(rook, Rook)
    assert rook.get_color() == PieceColor.BLACK
    assert rook.get_row() == 0
    assert rook.get_column() == 4


@pytest.fixture
def rook_test():
    return Rook.create_rook(PieceColor.WHITE, 1, 1)


def test_rook_initialization(rook_test):
    """Test that the rook class is initialized with the correct
       color, row and col.
    """
    assert isinstance(rook_test, Rook)
    assert rook_test._color == PieceColor.WHITE
    assert rook_test._current_row == 1
    assert rook_test._current_col == 1


def test_rook_get_color_method(rook_test):
    """Test the get_color method of the rook class."""
    assert rook_test.get_color() == PieceColor.WHITE
    assert rook_test.get_color() != PieceColor.BLACK


def test_rook_get_row_method(rook_test):
    """Test the get_row method of the rook class."""
    assert rook_test.get_row() == 1


def test_rook_get_col_method(rook_test):
    """Test the get_col method of the rook class."""
    assert rook_test.get_column() == 1
