from abc import ABC, abstractmethod

from src.pieces import Piece
from src.piece_manager import PieceManager
from src.players import Player
from src.rules.rule import Rule


class RuleHandler(Rule):
    def __init__(self, piece_manager: PieceManager):
        super().__init__(piece_manager)
        self._next_rule = None

    def set_next(self, rule: Rule) -> Rule:
        self._next_rule = rule
        return rule

    @abstractmethod
    def validate(self, piece: Piece, player: Player, target_row: int,
                 target_col: int) -> bool:
        if self._next_rule:
            return self._next_rule.validate(piece, player, target_row,
                                            target_col)
        return True
