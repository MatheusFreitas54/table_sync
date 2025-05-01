from pymongo import MongoClient
from models.nosql.feedback import Feedback

client = MongoClient('mongodb://localhost:27017')
db = client['feedback_db']
collection = db['feedbacks']

def carregar_feedbacks(df):

    for _, row in df.iterrows():
        feedback = Feedback(
            data=row['data'],
            feedback=row['feedback'],
            vendas_total=row['vendas_total'],
            prato_mais_vendido=row['prato_mais_vendido']
        ).to_dict()

        collection.insert_one(feedback)
