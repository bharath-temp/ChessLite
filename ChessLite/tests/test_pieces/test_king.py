import pytest

from src.pieces.king import King
from src.pieces.piece_factory import PieceFactory
from src.utils.colors import PieceColor
from src.utils.piece_type import PieceType


def test_king_factory_method():
    """Test the create_king factory method."""
    king = PieceFactory.create_piece(PieceType.KING, PieceColor.BLACK, 0, 4)
    assert isinstance(king, King)
    assert king.color == PieceColor.BLACK
    assert king.row == 0
    assert king.column == 4


@pytest.fixture
def king_test():
    return PieceFactory.create_piece(PieceType.KING, PieceColor.WHITE, 1, 1)


def test_king_initialization(king_test):
    """Test that the king class is initialized with the correct
       color, row and col.
    """
    assert isinstance(king_test, King)
    assert king_test._color == PieceColor.WHITE
    assert king_test._current_row == 1
    assert king_test._current_col == 1


def test_king_get_color_method(king_test):
    """Test the get_color method of the king class."""
    assert king_test.color == PieceColor.WHITE
    assert king_test.color != PieceColor.BLACK


def test_king_get_row_method(king_test):
    """Test the get_row method of the king class."""
    assert king_test.row == 1


def test_king_get_col_method(king_test):
    """Test the get_col method of the king class."""
    assert king_test.column == 1


def test_king_set_row_method(king_test):
    """Test the set_row method of the king class."""
    king_test.row = 2
    assert king_test.row == 2


def test_king_set_col_method(king_test):
    """Test the set_column method of the king class."""
    king_test.column = 3
    assert king_test.column == 3


def test_king_set_moved_method(king_test):
    """Test the set_moved method of the King class."""
    assert not king_test.moved  # Initially should be False
    king_test.moved = True
    assert king_test.moved  # After setting should be True
