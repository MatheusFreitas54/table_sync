from pydantic import BaseModel
from datetime import datetime

class Feedback(BaseModel):
   id_csv: int
   data: datetime
   feedback: str
   vendas_total: float
   prato_mais_vendido: str

   def to_dict(self):
      return {
         "id_csv": self.id_csv,
         "data": self.data.isoformat(),
         "feedback": self.feedback,
         "vendas_total": self.vendas_total,
         "prato_mais_vendido": self.prato_mais_vendido
      }