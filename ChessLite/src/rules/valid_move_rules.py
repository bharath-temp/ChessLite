from src.rules.helper_rules import CheckedHelperRule, PathClearHelperRule
from src.pieces import Piece
from src.piece_manager import PieceManager
from src.players import Player
from src.rules.rule_handler import RuleHandler
from src.utils import PieceColor, PieceType, PlayerType

class SameColorRule(RuleHandler):
    def validate(self, piece: Piece, player: Player, target_row: int,
                 target_col: int) -> bool:
        if piece.color is not player.color:
            print(f"Can't move opposite color piece")
            return False
        else:
            return super().validate(piece, player, target_row, target_col)


class FundPieceMoveRule(RuleHandler):
    def validate(self, piece: Piece, player: Player, target_row: int,
                 target_col: int) -> bool:
        if not piece._validate_piece_move(target_row, target_col):
            print(f"Can't move piece that way")
            return False
        return super().validate(piece, player, target_row, target_col)


class PathClearRule(RuleHandler):
    def __init__(self, piece_manager: PieceManager,
                 path_clear_rule: PathClearHelperRule) -> None:
        super().__init__(piece_manager)
        self._path_clear_rule = path_clear_rule

    def validate(self, piece: Piece, player: Player, target_row: int,
                 target_col: int) -> bool:
        if not self._path_clear_rule.validate(piece, player, target_row,
                                              target_col):
            print(f"Path for piece not clear")
            return False
        return super().validate(piece, player, target_row, target_col)


class SelfCheckRule(RuleHandler):
    def __init__(self, piece_manager: PieceManager,
                 checked_rule: CheckedHelperRule) -> None:
        super().__init__(piece_manager)
        self._checked_rule = checked_rule

    def validate(self, piece: Piece, player: Player, target_row: int,
                 target_col: int) -> bool:
        original_row = piece.row
        original_col = piece.column
        self._piece_manager.place_piece_at(piece, target_row, target_col)
        if self._checked_rule.validate(player):
            self._piece_manager.place_piece_at(piece, original_row,
                                                original_col)
            print(f"Move will cause self check")
            return False

        self._piece_manager.place_piece_at(piece, original_row,
                                            original_col)
        return super().validate(piece, player, target_row, target_col)
