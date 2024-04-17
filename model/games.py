from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime
from model.base import Base


class Game(Base):
    """
        Tabela: Game

        Colunas:

        id: Identificador único das tuplas.
        name: Nome do jogo.
        insertion_date: Data e hora da inserção do registro.
    """
    __tablename__ = 'game'

    id = Column("pk_game", Integer, primary_key=True)
    name = Column(String(50), unique=True)
    insertion_date = Column(DateTime, default=datetime.now())

    def __init__(self, name: str, insertion_date: datetime = None):
        self.name = name
        if insertion_date:
            self.insertion_date = insertion_date
