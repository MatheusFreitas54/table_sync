import streamlit as st
import pandas as pd
import plotly.express as px
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.analytics.consultas import (
    consultar_pratos_mais_vendidos,
    consultar_media_vendas_por_produto
)

st.title("📊 Dashboard - Análise de Vendas")

st.header("Top 5 Pratos Mais Vendidos 🍽️")
dados = consultar_pratos_mais_vendidos()
df_vendas = pd.DataFrame(dados, columns=["Produto", "Total de Vendas"])
fig_vendas = px.bar(df_vendas, x="Produto", y="Total de Vendas", color="Produto", title="Pratos Mais Vendidos")
st.plotly_chart(fig_vendas)

st.header("Média de Vendas por Produto 🛒")
medias = consultar_media_vendas_por_produto()
df_medias = pd.DataFrame(medias, columns=["Produto", "Média de Venda"])
fig_media = px.pie(df_medias, names="Produto", values="Média de Venda", title="Média de Venda por Produto")
st.plotly_chart(fig_media)
