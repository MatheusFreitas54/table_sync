import pandas as pd

def ler_clientes(path='backend/data/clientes.csv'):
    return pd.read_csv(path)

def ler_pedidos(path='backend/data/pedidos.csv'):
    return pd.read_csv(path)