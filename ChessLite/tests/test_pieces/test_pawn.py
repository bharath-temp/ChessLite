import pytest

from src.pieces.pawn import Pawn
from src.pieces.piece_factory import PieceFactory
from src.utils.colors import PieceColor
from src.utils.piece_type import PieceType


def test_pawn_factory_method():
    """Test the create_pawn factory method."""
    pawn = PieceFactory.create_piece(PieceType.PAWN,
                                     PieceColor.BLACK, 0, 4)
    assert isinstance(pawn, Pawn)
    assert pawn.color == PieceColor.BLACK
    assert pawn.row == 0
    assert pawn.column == 4


@pytest.fixture
def pawn_test():
    return PieceFactory.create_piece(PieceType.PAWN, PieceColor.WHITE, 1, 1)


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
    assert pawn_test.color == PieceColor.WHITE
    assert pawn_test.color != PieceColor.BLACK


def test_pawn_get_row_method(pawn_test):
    """Test the get_row method of the pawn class."""
    assert pawn_test.row == 1


def test_pawn_get_col_method(pawn_test):
    """Test the get_col method of the pawn class."""
    assert pawn_test.column == 1


def test_pawn_set_row_method(pawn_test):
    """Test the set_row method of the pawn class."""
    pawn_test.row = 2
    assert pawn_test.row == 2


def test_pawn_set_col_method(pawn_test):
    """Test the set_column method of the pawn class."""
    pawn_test.column = 3
    assert pawn_test.column == 3


def test_pawn_set_moved_method(pawn_test):
    """Test the set_moved method of the pawn class."""
    assert not pawn_test.moved  # Initially should be False
    pawn_test.moved = True
    assert pawn_test.moved  # After setting should be True
