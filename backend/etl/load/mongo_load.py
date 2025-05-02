import sys

from pymongo import MongoClient
from models.nosql.feedback import Feedback

client = MongoClient('mongo')
db = client['feedback_db']
collection = db['feedbacks']

collection.create_index("id_csv", unique=True)

def carregar_feedbacks(df):
    novos_feedbacks = []

    for _, row in df.iterrows():
        existente = collection.find_one({"id_csv": row['id']})
        if not existente:
            fb = Feedback(
                id_csv=row['id'],
                data=row['data'],
                feedback=row['feedback'],
                vendas_total=row['vendas_total'],
                prato_mais_vendido=row['prato_mais_vendido']
            )
            novos_feedbacks.append(fb.to_dict())

    if novos_feedbacks:
        collection.insert_many(novos_feedbacks)
        print(f"{len(novos_feedbacks)} feedback(s) inserido(s) no MongoDB.")
    else:
        print("Nenhum novo feedback para inserir.")
