from sqlalchemy import Column, Integer, String
from core.database import Base

class Funcionario(Base):
    __tablename__ = "funcionarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_csv = Column(Integer, index=True)  # ID original do CSV
    nome = Column(String)
    cargo = Column(String)
    turno = Column(String)
