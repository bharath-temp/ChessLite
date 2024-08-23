from __future__ import annotations
from typing import override

from src.players.player import Player
from src.utils.player_type import PlayerType
from src.utils.colors import PieceColor


class HumanPlayer(Player):
    """A class representing a human player in a chess game.

    Inherits from the Player abstract base class and implements the properties
    specific to a human player.

    Attributes:
        _name (str): The name of the human player.
        _player_type (PlayerType): The type of the player (HUMAN).
        _color (PieceColor): The color of the human player's pieces.
    """

    def __init__(self, color: PieceColor, name: str = None) -> None:
        """Initializes a human player with the specified color and optional
           name.

        Args:
            color (PieceColor): The color of the human player's pieces.
            name (str, optional): The name of the human player. If not
                                  provided, a default name is generated based
                                  on the player type and color.
        """
        super().__init__(PlayerType.HUMAN, color, name)

    @staticmethod
    def create_human_player(color: PieceColor,
                            name: str = None) -> HumanPlayer:
        """Factory method to create a human player.

        Args:
            color (PieceColor): The color of the human player's pieces.
            name (str, optional): The name of the human player. If not
                                  provided, a default name is generated based
                                  on the player type and color.

        Returns:
            HumanPlayer: A new instance of HumanPlayer.
        """
        return HumanPlayer(color, name)

    @override
    @property
    def player_type(self) -> PlayerType:
        """The type of the player (HUMAN)."""
        return self._player_type

    @override
    @property
    def name(self) -> str:
        """The name of the human player."""
        return self._name

    @override
    @property
    def color(self) -> PieceColor:
        """The color of the human player's pieces."""
        return self._color
