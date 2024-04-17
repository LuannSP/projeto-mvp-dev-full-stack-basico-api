from pydantic import BaseModel
from typing import List
from model.games import Game


class GameSchema(BaseModel):
    name: str = "Game Name"


class GameSearchSchema(BaseModel):
    name: str = "Game Name"


class ListGameSchema(BaseModel):
    games: List[GameSchema]


class GameViewSchema(BaseModel):
    id: int = 1
    name: str = "Game Name"


class GameDelSchema(BaseModel):
    name: str
    message: str


def present_games(games: List[Game]):
    result = []
    for game in games:
        result.append({
            "name": game.name,
        })

    return {"games": result}


def present_game(game: Game):
    return {
        "id": game.id,
        "name": game.name,
    }
