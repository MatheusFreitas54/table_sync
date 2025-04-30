from core.database import Base, engine
from models.cliente import Cliente
from models.pedido import Pedido
from models.funcionario import Funcionario

# Criação das tabelas no banco SQLite
def criar_tabelas():
   Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
   criar_tabelas()