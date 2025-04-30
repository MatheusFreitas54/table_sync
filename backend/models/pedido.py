from sqlalchemy import Column, Integer, Float, String, Date, ForeignKey
from core.database import Base

class Pedido(Base):
   __tablename__ = "pedidos"

   id = Column(Integer, primary_key=True, autoincrement=True)
   id_csv = Column(Integer, index=True)
   client_id = Column(Integer, ForeignKey("clientes.id"))  # Chave estrangeira para Cliente
   produto = Column(String)
   quantidade = Column(Integer)
   preco_unitario = Column(Float)
   total_pedido = Column(Float)
   data_pedido = Column(Date)
   status_pedido = Column(String)
