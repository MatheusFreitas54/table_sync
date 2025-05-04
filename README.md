# 📊 Table Sync

Plataforma analítica para restaurantes que centraliza dados operacionais de diversas fontes (CSV, SQLite, MongoDB) em dashboards interativos. Facilita a visualização de métricas como desempenho de funcionários, satisfação de clientes e histórico de pedidos.

## 📁 Estrutura do Projeto

```
.
.
├── .gitignore
├── Dockerfile
├── README.md
├── docker-compose.yml
├── requirements.txt
├── frontend
│   └── dashboard.py
└── backend
    ├── main.py
    ├── dados.sqlite3
    ├── core
    │   ├── config.py
    │   └── database.py
    ├── data
    │   ├── clientes.csv
    │   ├── feedbacks.csv
    │   ├── funcionarios.csv
    │   └── pedidos.csv
    ├── etl
    │   ├── __init__.py
    │   ├── extract.py
    │   ├── run_etl.py
    │   ├── transform.py
    │   └── load
    │       ├── __init__.py
    │       ├── mongo_load.py
    │       └── sql_load.py
    ├── analytics
    │   ├── __init__.py
    │   ├── consultas.py
    │   ├── run_analytics.py
    │   └── validacao.py
    ├── app
    │   └── api
    │       └── routes
    │           ├── clientes.py
    │           ├── feedbacks.py
    │           └── pedidos.py
    └── models
        ├── nosql
        │   ├── __init__.py
        │   └── feedback.py
        └── sql
            ├── __init__.py
            ├── cliente.py
            ├── funcionario.py
            └── pedido.py

```

---

## 🚀 Funcionalidades

- 🔄 **Pipeline ETL** para transformar e unificar dados de diversas fontes  
- 📥 **Importação automática** de CSV para bancos SQL e MongoDB  
- 📊 **Consultas analíticas** com filtros e validações embutidas  
- 📈 **Dashboard Interativo** com métricas visuais (Streamlit)
- 🔍 **Análises avançadas** por desempenho, avaliação e histórico

---

## 🛠️ Stack & Execução

---

| Camada     | Tecnologia                              |
|------------|-----------------------------------------|
| Front‑end  | Streamlit (dashboard interativo)        |
| Back‑end   | Python 3.11 · FastAPI · Pydantic        |
| Banco SQL  | SQLite (relacional local)               |
| Banco NoSQL| MongoDB / Docker                        |
| Deploy     | Docker + Docker Compose                 |

---

1. **Clone o repositório**
   ```bash
   git clone https://github.com/MatheusFreitas54/table_sync.git
   cd table_sync
   ```
   
2. **Suba tudo com Docker (recomendado)**

   ```bash
   docker compose up -d --build
   ```

3. **Rodar localmente sem Docker (opcional)**

   `Backend`

   ```bash
   cd backend
   python -m venv .venv && source .venv/bin/activate
   pip install -r ../requirements.txt
   ```

   `ETL`

   ```bash
   venv/bin/python backend/main.py
   venv/bin/python backend/etl/run_etl.py
   ```

   `FrontEnd`

   ```bash
   cd frontend
   streamlit run dashboard.py
   ```

  

---

## 🧠 Conceitos Utilizados

   - Arquitetura modular com camadas: ETL · API · Analytics · Dashboard
   - Banco híbrido: SQLite (operacional) + MongoDB (qualitativo)
   - Streamlit para visualização de dados em tempo real
   - Transformações de dados robustas com validação e enriquecimento
   - Containerização com Docker + docker-compose

---

## 🔧 Melhorias Futuras

   - Agendamento automático do ETL com Airflow ou cron
   - Filtros interativos no dashboard por período e tipo de métrica
   - Exportação de relatórios em PDF diretamente pelo dashboard

---

## Autores

Desenvolvido por Matheus Freitas ™