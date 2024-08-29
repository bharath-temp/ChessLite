from src.game_board import GameBoard
from src.game_controller import GameController
from src.piece_manager import PieceManager
from src.players import Player, AIPlayer, HumanPlayer, PlayerFactory
from src.utils import PieceColor, PieceType, PlayerType


def main():
    player_one = PlayerFactory.create_player(PlayerType.HUMAN,
                                             PieceColor.WHITE, "Bob")
    player_two = PlayerFactory.create_player(PlayerType.HUMAN,
                                             PieceColor.BLACK, "Alice")

    piece_manager = PieceManager()
    board = GameBoard(piece_manager)
    game_controller = GameController(piece_manager, player_one, player_two)
    # 6 5 5 5
    # 1 4 3 4
    # 6 6 4 6
    # 0 3 4 7

    while not game_controller.is_game_over():
        print("in main")

        if game_controller.is_checkmate():
            break

        current_player = game_controller._GameController__current_player
        print(
            f"{current_player.name}'s turn ({current_player.color.name})."
        )

        move_input = input(
            "Enter your move (format: start_row start_col end_row end_col): "
        )

        try:
            start_row, start_col, end_row, end_col = map(int,
                                                         move_input.split())
        except ValueError:
            print(
                    f"Invalid input format. Please enter four"
                    f"integers separated by spaces."
                 )
            continue

        game_controller.get_player_input(start_row, start_col,
                                         end_row, end_col)
        board.update_board()
        board.display_board()

    '''
    board.update_board()
    board.display_board()
    game_controller.validate_player_move(2,0,1,1)
    game_controller.validate_player_move(0,3,1,1)
    game_controller.validate_player_move(7,3,8,3)
    game_controller.validate_player_move(7,3,3,7)
    board.update_board()
    board.display_board()
    '''


if __name__ == "__main__":
    main()
