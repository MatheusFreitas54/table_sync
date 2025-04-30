from sqlalchemy import Column, Integer, String, Date
from core.database import Base

class Cliente(Base):
   __tablename__ = "clientes"

   id = Column(Integer, primary_key=True, autoincrement=True)
   id_csv = Column(Integer, index=True)
   nome = Column(String)
   email = Column(String, unique=True, index=True)
   data_nascimento = Column(Date)
   cpf = Column(String, unique=True)
