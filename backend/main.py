from core.database import Base, engine
from models.sql.cliente import Cliente
from models.sql.pedido import Pedido
from models.sql.funcionario import Funcionario

# Criação das tabelas no banco SQLite
def criar_tabelas():
   Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
   criar_tabelas()