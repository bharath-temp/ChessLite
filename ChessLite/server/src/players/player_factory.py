from src.utils.colors import PieceColor
from src.players.player import Player
from src.utils.player_type import PlayerType


class PlayerFactory():
    """Factory class for creating and registering chess players.

    This class manages the registration and creation of chess player instances
    based on the provided player type. Players are registered using the
    `register_player` class method and can be created using the `create_player`
    static method.
    """

    __player_registry = {}

    @classmethod
    def register_player(cls, player_type: PlayerType):
        """Decorator to register a chess player class with the factory.

        This method returns a decorator that registers the provided player
        class with the factory under the specified player type.

        Args:
            player_type (PlayerType): The type of chess player to register.

        Returns:
            function: A decorator function that registers the player class.
        """
        def wrapper(player: Player):
            if player_type not in cls.__player_registry:
                cls.__player_registry[player_type] = player

            return player

        return wrapper

    @staticmethod
    def create_player(player_type: PlayerType, color: PieceColor,
                      name: str = None):
        """Creates an instance of a registered chess player.

        This method retrieves the class associated with the specified player
        type from the registry and creates an instance of it using the
        provided color and optional name.

        Args:
            player_type (PlayerType): The type of chess player to create.
            color (PieceColor): The color of the chess player's pieces.
            name (str, optional): The name of the chess player. Defaults
                                  to None.

        Returns:
            Player: An instance of the requested chess player.

        Raises:
            ValueError: If the player type is not registered.
        """
        player_class = PlayerFactory.__player_registry.get(player_type)
        if not player_class:
            raise ValueError(f"Piece type {player_type} is not registered.")

        return player_class(color, name)
