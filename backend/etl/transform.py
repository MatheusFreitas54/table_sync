import pandas as pd

def remover_duplicados_clientes(df):
   df_sem_duplicatas = df.drop_duplicates(subset='cpf', keep='first')
   return df_sem_duplicatas

def transformar_clientes(df):
   df['nome'] = df['nome'].str.title()
   df['email'] = df['email'].str.lower()
   df['data_nascimento'] = pd.to_datetime(df['data_nascimento'], errors='coerce')
   return df

def transformar_pedidos(df):
   df['data_pedido'] = pd.to_datetime(df['data_pedido'], errors='coerce')
   return df

def transformar_funcionarios(df):
   df['nome'] = df['nome'].str.title()
   df['cargo'] = df['cargo'].str.title()
   df['turno'] = df['turno'].str.title()
   return df