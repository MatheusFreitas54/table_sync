from sqlalchemy.orm import Session
from core.database import SessionLocal
from models.sql.cliente import Cliente
from models.sql.pedido import Pedido
from models.sql.funcionario import Funcionario

def carregar_clientes(df):
   with SessionLocal() as db:
      for _, row in df.iterrows():
         cpf_existente = db.query(Cliente).filter_by(cpf=row['cpf']).first()
         if not cpf_existente:
            cliente = Cliente(
               id_csv=row['id'],
               nome=row['nome'],
               email=row['email'],
               data_nascimento=row['data_nascimento'],
               cpf=row['cpf']
            )
         db.add(cliente)
      db.commit()

def carregar_pedidos(df):
   with SessionLocal() as db:
      for _, row in df.iterrows():
         pedido = Pedido(
               id_csv=row['id'],
               client_id=row['client_id'],
               produto=row['produto'],
               quantidade=row['quantidade'],
               preco_unitario=row['preco_unitario'],
               total_pedido=row['total_pedido'],
               data_pedido=row['data_pedido'],
               status_pedido=row['status_pedido']
         )
         db.merge(pedido)
      db.commit()

def carregar_funcionarios(df):
   with SessionLocal() as db:
      for _, row in df.iterrows():
         funcionario = Funcionario(
               id_csv=row['id'],
               nome=row['nome'],
               cargo=row['cargo'],
               turno=row['turno']
         )
         db.add(funcionario)
      db.commit()