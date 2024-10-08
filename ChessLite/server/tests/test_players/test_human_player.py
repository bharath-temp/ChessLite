import pytest

from src.players import HumanPlayer, PlayerFactory
from src.utils import PieceColor, PlayerType


def test_human_player_factory_method():
    human_player = PlayerFactory.create_player(PlayerType.HUMAN,
                                               PieceColor.BLACK)
    assert isinstance(human_player, HumanPlayer)
    assert human_player.player_type == PlayerType.HUMAN
    assert human_player.color == PieceColor.BLACK
    assert human_player.name == (
        f"{human_player.player_type.name.lower()}_"
        f"{human_player.color.name.lower()}"
    )
