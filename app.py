from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote
from sqlalchemy.exc import IntegrityError
from model.games import Game
from model import Session
from schemas import *
from flask_cors import CORS

info = Info(title="GAMER API MVP", version="1.0.0")
app = OpenAPI(__name__, info=info)
home_tag = Tag(name="Documentação",description="Seleção automática do estilo de documentação Swagger.")
game_tag = Tag(name="Game", description="Adicionando, visualizando, removendo e buscando jogos no banco de dados.")
CORS(app)


@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi/swagger, o estilo de documentação a ser exibido.
    """
    return redirect('/openapi/swagger')


@app.get('/game', tags=[game_tag], responses={"200": GameViewSchema, "404": ErrorSchema})
def get_game(query: GameSearchSchema):
    """Realiza uma busca por todos os jogos no banco de dados pelo nome.
    """
    game_id = query.name
    session = Session()
    game = session.query(Game).filter(Game.name == game_id).first()

    if game:
        return present_game(game), 200
    else:
        error_msg = "Game not found in the database."
        return {"message": error_msg}, 404


@app.get('/games', tags=[game_tag], responses={"200": ListGameSchema, "404": ErrorSchema})
def get_games():
    """Realiza uma busca por todos os jogos no banco de dados.
    """
    session = Session()
    games = session.query(Game).all()

    if not games:
        return {"games": []}, 200
    else:
        return present_games(games), 200


@app.post('/games', tags=[game_tag], responses={"200": GameViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_game(form: GameSchema):
    """Adiciona um novo jogo ao banco de dados.
    """
    game = Game(
        name=form.name)
    try:
        session = Session()
        session.add(game)
        session.commit()
        return present_game(game), 200

    except IntegrityError as e:
        error_msg = "Game with the same name already saved in the database."
        return {"message": error_msg}, 409

    except Exception as e:
        error_msg = "Could not save a new game."
        return {"message": error_msg}, 400


@app.delete('/games', tags=[game_tag], responses={"200": GameDelSchema, "404": ErrorSchema})
def del_games(query: GameSearchSchema):
    """Exclui um jogo específico do banco de dados, com base no nome fornecido.
    """
    game_name = unquote(unquote(query.name))
    print(game_name)
    session = Session()
    count = session.query(Game).filter(Game.name == game_name).delete()
    session.commit()

    if count:
        return {"name": game_name, "message": "Game removed"}
    else:
        error_msg = "Game not found in the database."
        return {"message": error_msg}, 404
