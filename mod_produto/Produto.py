from pydantic import BaseModel

class Produto(BaseModel):
    id_funcionario: int = None
    nome: str
    valor_unitario: int
    descricao: str
   