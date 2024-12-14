from typing import override

from src.rules.helper_rules import CheckedHelperRule, PathClearHelperRule
from src.pieces import Piece
from src.piece_manager import PieceManager
from src.players import Player
from src.rules.rule_handler import RuleHandler
from src.utils import PieceColor, PieceType, PlayerType


class SameColorRule(RuleHandler):
    @override
    def validate(self, piece: Piece, player: Player, target_row: int,
                 target_col: int) -> bool:
        if piece.color is not player.color:
            print(f"Can't move opposite color piece")
            return False
        else:
            return super().validate(piece, player, target_row, target_col)


class FundPieceMoveRule(RuleHandler):
    @override
    def validate(self, piece: Piece, player: Player, target_row: int,
                 target_col: int) -> bool:
        if not piece._validate_piece_move(target_row, target_col):
            return False
        return super().validate(piece, player, target_row, target_col)


class PathClearRule(RuleHandler):
    def __init__(self, piece_manager: PieceManager,
                 path_clear_rule: PathClearHelperRule) -> None:
        super().__init__(piece_manager)
        self._path_clear_rule = path_clear_rule

    @override
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

    @override
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


class CapturePieceRule(RuleHandler):
    def __init__(self, piece_manager: PieceManager) -> None:
        super().__init__(piece_manager)

    @override
    def validate(self, piece: Piece, player: Player, target_row: int,
                 target_col: int) -> bool:
        target_piece = self._piece_manager.get_piece_at(target_row, target_col)

        if piece.piece_type is PieceType.PAWN:
            if not self.__pawn_capture_rule(piece, target_piece,
                                            target_row, target_col):
                return False

        if (target_piece is None) or (target_piece.color != piece.color):
            return super().validate(piece, player, target_row, target_col)

        return False

    def __pawn_capture_rule(self, piece: Piece, target_piece: Piece,
                            target_row: int, target_col: int) -> bool:
        row_diff = abs(piece.row - target_row)
        col_diff = abs(piece.column - target_col)

        if row_diff == 1 and col_diff == 1:
            if target_piece is None or target_piece.color == piece.color:
                return False

        return True
