import pytest

from src.players import AIPlayer, PlayerFactory
from src.utils import PieceColor, PlayerType


def test_ai_player_factory_method():
    ai_player = PlayerFactory.create_player(PlayerType.AI, PieceColor.BLACK)
    assert isinstance(ai_player, AIPlayer)
    assert ai_player.player_type == PlayerType.AI
    assert ai_player.color == PieceColor.BLACK
    assert ai_player.name == (
        f"{ai_player.player_type.name.lower()}_"
        f"{ai_player.color.name.lower()}"
    )
