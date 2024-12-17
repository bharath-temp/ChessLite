from abc import ABC, abstractmethod

from src.pieces import Piece
from src.players import Player
from src.piece_manager import PieceManager


class Rule(ABC):
    """
    Base class for all rules, both those in the chain and special rules like
    castling and promotion.
    """

    def __init__(self, piece_manager: PieceManager) -> None:
        self._piece_manager = piece_manager

    @abstractmethod
    def validate(self, piece: Piece, player: Player, target_row: int,
                 target_col: int) -> bool:
        """
        Validate the move according to this rule.
        Should return True if the rule is satisfied, otherwise False.
        """
        pass
