from pydantic import BaseModel

class Produto(BaseModel):
    id_produto: int = None
    nome: str
    valor_unitario: int
    descricao: str
   