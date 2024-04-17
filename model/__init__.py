from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database

from model.base import Base
from model.games import Game

db_path = Path("database")
db_path.mkdir(parents=True, exist_ok=True)

db_url = 'sqlite:///' + str(db_path / "database_games.sqlite3")

engine = create_engine(db_url, echo=False)

Session = sessionmaker(bind=engine)

try:
    create_database(engine.url)
except Exception as e:
    print(f"O banco de dados já existe: {e}")

Base.metadata.create_all(engine)
