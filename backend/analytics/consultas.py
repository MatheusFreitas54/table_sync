import sqlite3

def consultar_pratos_mais_vendidos():
   conn = sqlite3.connect('backend/dados.sqlite3')
   cursor = conn.cursor()

   query = """
   SELECT produto, SUM(quantidade) AS total_vendas
   FROM pedidos
   GROUP BY produto
   ORDER BY total_vendas DESC
   LIMIT 5;
   """
   cursor.execute(query)
   resultados = cursor.fetchall()
   conn.close()

   return resultados

def consultar_media_vendas():
   conn = sqlite3.connect('backend/dados.sqlite3')
   cursor = conn.cursor()

   query = """
   SELECT AVG(total_pedido) FROM pedidos;
   """
   cursor.execute(query)
   resultado = cursor.fetchone()
   conn.close()

   return resultado[0]