import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from etl.extract import ler_clientes, ler_pedidos, ler_funcionarios, ler_feedbacks
from etl.transform import (
   transformar_clientes, transformar_pedidos, transformar_funcionarios, transformar_feedbacks,
   remover_duplicados_clientes
)
from etl.load.sql_load import carregar_clientes, carregar_pedidos, carregar_funcionarios
from etl.load.mongo_load import carregar_feedbacks

def executar_etl():
   clientes = ler_clientes()
   pedidos = ler_pedidos()
   funcionarios = ler_funcionarios()
   feedbacks = ler_feedbacks()

   clientes = remover_duplicados_clientes(clientes)
   clientes = transformar_clientes(clientes)
   pedidos = transformar_pedidos(pedidos)
   funcionarios = transformar_funcionarios(funcionarios)
   feedbacks = transformar_feedbacks(feedbacks)

   carregar_clientes(clientes)
   carregar_pedidos(pedidos)
   carregar_funcionarios(funcionarios)
   carregar_feedbacks(feedbacks)

   print(feedbacks.head()) 

if __name__ == "__main__":
   executar_etl()