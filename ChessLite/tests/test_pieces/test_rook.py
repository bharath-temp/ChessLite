import pytest

from src.pieces import Rook, PieceFactory
from src.utils import PieceColor, PieceType


def test_rook_factory_method():
    """Test the create_rook factory method."""
    rook = PieceFactory.create_piece(PieceType.ROOK, PieceColor.BLACK, 0, 4)
    assert isinstance(rook, Rook)
    assert rook.color == PieceColor.BLACK
    assert rook.row == 0
    assert rook.column == 4


@pytest.fixture
def rook_test():
    return PieceFactory.create_piece(PieceType.ROOK, PieceColor.WHITE, 1, 1)


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
    assert rook_test.color == PieceColor.WHITE
    assert rook_test.color != PieceColor.BLACK


def test_rook_get_row_method(rook_test):
    """Test the get_row method of the rook class."""
    assert rook_test.row == 1


def test_rook_get_col_method(rook_test):
    """Test the get_col method of the rook class."""
    assert rook_test.column == 1


def test_rook_set_row_method(rook_test):
    """Test the set_row method of the rook class."""
    rook_test.row = 2
    assert rook_test.row == 2


def test_rook_set_col_method(rook_test):
    """Test the set_column method of the rook class."""
    rook_test.column = 3
    assert rook_test.column == 3


def test_rook_set_moved_method(rook_test):
    """Test the set_moved method of the rook class."""
    assert not rook_test.moved  # Initially should be False
    rook_test.moved = True
    assert rook_test.moved  # After setting should be True
