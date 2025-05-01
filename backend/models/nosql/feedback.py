from pydantic import BaseModel
from datetime import datetime

class Feedback(BaseModel):
   data: datetime
   feedback: str
   vendas_total: float
   prato_mais_vendido: str

   def to_dict(self):
      return {
         "data": self.data.isoformat(),
         "feedback": self.feedback,
         "vendas_total": self.vendas_total,
         "prato_mais_vendido": self.prato_mais_vendido
      }