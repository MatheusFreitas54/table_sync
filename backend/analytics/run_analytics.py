from consultas import consultar_pratos_mais_vendidos, consultar_media_vendas
from validacao import verificar_duplicados, verificar_nulos

def executar_analises():
   print("Iniciando análises e validações de dados...\n")

   pratos_mais_vendidos = consultar_pratos_mais_vendidos()
   print("Pratos mais vendidos:", pratos_mais_vendidos)

   media_vendas = consultar_media_vendas()
   print("Média de vendas:", media_vendas)

   duplicados = verificar_duplicados()
   if duplicados:
      print(f"Existem {len(duplicados)} registros duplicados.")
   else:
      print("Não existem registros duplicados.")

   nulos = verificar_nulos()
   print(f"Existem {nulos} registros com valores nulos.")

if __name__ == "__main__":
   executar_analises()