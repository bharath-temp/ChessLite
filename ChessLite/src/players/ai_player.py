from __future__ import annotations
from typing import override

from src.players.player import Player
from src.utils.player_type import PlayerType
from src.utils.colors import PieceColor


class AIPlayer(Player):
    """A class representing an AI player in a chess game.

    Inherits from the Player abstract base class and implements the properties
    specific to an AI player.

    Attributes:
        _name (str): The name of the AI player.
        _player_type (PlayerType): The type of the player (AI).
        _color (PieceColor): The color of the AI player's pieces.
    """

    def __init__(self, color: PieceColor, name: str = None) -> None:
        """Initializes an AI player with the specified color and optional name.

        Args:
            color (PieceColor): The color of the AI player's pieces.
            name (str, optional): The name of the AI player. If not provided,
                                  a default name is generated based on the
                                  player type and color.
        """
        super().__init__(PlayerType.AI, color, name)

    @staticmethod
    def create_ai_player(color: PieceColor, name: str = None) -> AIPlayer:
        """Factory method to create an AI player.

        Args:
            color (PieceColor): The color of the AI player's pieces.
            name (str, optional): The name of the AI player. If not provided,
                                  a default name is generated based on the
                                  player type and color.

        Returns:
            AIPlayer: A new instance of AIPlayer.
        """
        return AIPlayer(color, name)

    @override
    @property
    def player_type(self) -> PlayerType:
        """The type of the player (AI)."""
        return self._player_type

    @override
    @property
    def name(self) -> str:
        """The name of the AI player."""
        return self._name

    @override
    @property
    def color(self) -> PieceColor:
        """The color of the AI player's pieces."""
        return self._color
