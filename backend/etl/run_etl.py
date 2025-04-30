import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from etl.extract import ler_clientes, ler_pedidos, ler_funcionarios
from etl.transform import (
   transformar_clientes, transformar_pedidos, transformar_funcionarios,
   remover_duplicados_clientes
)
from etl.load import carregar_clientes, carregar_pedidos, carregar_funcionarios

def executar_etl():
   clientes = ler_clientes()
   pedidos = ler_pedidos()
   funcionarios = ler_funcionarios()

   clientes = remover_duplicados_clientes(clientes)
   clientes = transformar_clientes(clientes)
   pedidos = transformar_pedidos(pedidos)
   funcionarios = transformar_funcionarios(funcionarios)

   carregar_clientes(clientes)
   carregar_pedidos(pedidos)
   carregar_funcionarios(funcionarios)

if __name__ == "__main__":
   executar_etl()