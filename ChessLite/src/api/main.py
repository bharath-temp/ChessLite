from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from uuid import uuid4

from src.game_board import GameBoard
from src.game_controller import GameController
from src.piece_manager import PieceManager
from src.players import Player, AIPlayer, HumanPlayer, PlayerFactory
from src.utils import PieceColor, PieceType, PlayerType

app = FastAPI()

class MoveInput(BaseModel):
    start_row: int
    start_col: int
    end_row: int
    end_col: int

games = {}


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/game_ids")
async def game_ids():
    return {"message": games}

@app.post("/new_game")
async def create_game(player_one_name: str, player_two_name: str):
    game_id = str(uuid4())

    player_one = PlayerFactory.create_player(PlayerType.HUMAN,
                                             PieceColor.WHITE, player_one_name)
    player_two = PlayerFactory.create_player(PlayerType.HUMAN,
                                             PieceColor.BLACK, player_two_name)
    piece_manager = PieceManager()
    game_controller = GameController(piece_manager, player_one, player_two)

    games[game_id] = game_controller

    return {
        "game_id": game_id,
        "message": "New game started",
        "player_one": player_one_name,
        "player_two": player_two_name,
        "board": game_controller.serialize_board_state()
    }


@app.post("/make_move/{game_id}")
async def make_move(game_id: str, input: MoveInput):
    game_controller = games[game_id]
    current_player = game_controller.get_current_player()

    game_controller.handle_player_input(input.start_row, input.start_col,
                                        input.end_row, input.end_col)

    next_player = game_controller.get_current_player()  # The opponent after the move

    # Check if the next player is in checkmate
    if game_controller.is_checkmate():
        return {
            "message": "Checkmate!",
            "loser": next_player.color.name,  # The opponent is the loser
            "board": game_controller.serialize_board_state()
        }

    return game_controller.serialize_board_state()

@app.get("/current_player/{game_id}")
async def get_current_player_color(game_id: str):
    game_controller = games[game_id]
    current_player = game_controller.get_current_player()
    return {"player_color": current_player.color.name}
    
