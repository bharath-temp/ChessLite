import pytest

from src.players.human_player import HumanPlayer
from src.utils.colors import PieceColor
from src.utils.player_type import PlayerType


def test_human_player_factory_method():
    human_player = HumanPlayer.create_human_player(PieceColor.BLACK)
    assert isinstance(human_player, HumanPlayer)
    assert human_player.player_type == PlayerType.HUMAN
    assert human_player.color == PieceColor.BLACK
    assert human_player.name == (
        f"{human_player.player_type.name.lower()}_"
        f"{human_player.color.name.lower()}"
    )
