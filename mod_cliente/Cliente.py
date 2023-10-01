from pydantic import BaseModel

class Cliente(BaseModel):
    id_cliente: int = None
    nome: str
    compra_fiado: int
    cpf: str
    telefone: str = None
    dia_fiado: int
    senha: str = None