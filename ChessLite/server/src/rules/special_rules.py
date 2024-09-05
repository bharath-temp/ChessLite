from typing import override

from src.pieces import Piece
from src.players import Player
from src.piece_manager import PieceManager
from src.pieces import Bishop, King, Knight, Pawn, \
                       Piece, PieceFactory, Queen, Rook
from src.rules.rule import Rule
from src.rules.rule_handler import RuleHandler
from src.rules.helper_rules import CheckedHelperRule, PathClearHelperRule


BOARD_SIZE = 8


class CheckMatedRule(Rule):
    def __init__(self, piece_manager: PieceManager,
                 checked_helper_rule: CheckedHelperRule,
                 rules_chain: RuleHandler) -> None:
        super().__init__(piece_manager)
        self._checked_helper_rule = checked_helper_rule
        self._rules_chain = rules_chain

    @override
    def validate(self, player: Player) -> bool:
        if not self._checked_helper_rule.validate(player):
            return False

        friendly_pieces = self._piece_manager.get_friendly_pieces(player.color)

        for piece in friendly_pieces:
            print(f"checking with: {piece} {piece.row} {piece.column}")
            for row in range(BOARD_SIZE):
                for col in range(BOARD_SIZE):
                    if self._rules_chain.validate(piece, player, row, col):
                        print(f"Uncheckmated with {piece} {row} {col}")
                        return False

        return True


class EnPessantRule(Rule):
    @override
    def validate(self, piece: Piece, player: Player, target_row: int,
                 target_col: int) -> bool:
        pass


class CastlingRule(Rule):
    @override
    def validate(self, piece: Piece, player: Player, target_row: int,
                 target_col: int) -> bool:
        pass
