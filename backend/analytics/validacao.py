import sqlite3

def verificar_duplicados():
   conn = sqlite3.connect('backend/dados.sqlite3')
   cursor = conn.cursor()

   query = """
   SELECT id_csv, COUNT(*) 
   FROM pedidos
   GROUP BY id
   HAVING COUNT(*) > 1;
   """
   cursor.execute(query)
   duplicados = cursor.fetchall() 
   conn.close()

   return duplicados

def verificar_nulos():
   conn = sqlite3.connect('backend/dados.sqlite3')
   cursor = conn.cursor()

   query = """
   SELECT COUNT(*) 
   FROM pedidos 
   WHERE produto IS NULL OR total_pedido IS NULL;
   """
   cursor.execute(query)
   nulos = cursor.fetchone()
   conn.close()

   return nulos[0]  