from abc import ABC, abstractmethod

from src.utils.colors import PieceColor
from src.utils.player_type import PlayerType


class Player(ABC):
    """Abstract base class for a player in a chess game.

    Attributes:
        _name (str): The name of the player.
        _player_type (PlayerType): The type of the player (e.g., human, AI).
        _color (PieceColor): The color of the player's pieces.
    """

    def __init__(self, player_type: PlayerType, color: PieceColor,
                 name: str = None) -> None:
        """Initializes a player with the specified type, color, and name.

        Args:
            player_type (PlayerType): The type of the player (e.g., human, AI).
            color (PieceColor): The color of the player's pieces.
            name (str, optional): The name of the player. If not provided,
                                  a default name is generated based on the
                                  player type and color.
        """
        if name is None:
            name = f"{player_type.name.lower()}_{color.name.lower()}"
        self._name = name
        self._player_type = player_type
        self._color = color

    @property
    @abstractmethod
    def player_type(self) -> PlayerType:
        """Abstract property to get the player's type.

        Returns:
            PlayerType: The type of the player (e.g., human, AI).
        """
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        """Abstract property to get the player's name.

        Returns:
            str: The name of the player.
        """
        pass

    @property
    @abstractmethod
    def color(self) -> PieceColor:
        """Abstract property to get the color of the player's pieces.

        Returns:
            PieceColor: The color of the player's pieces.
        """
        pass
