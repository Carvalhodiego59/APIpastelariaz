import db
from sqlalchemy import Column, VARCHAR, CHAR, Integer
# ORM

class ProdutoDB(db.Base):
    __tablename__ = 'tb_produto'
    id_cliente = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nome = Column(VARCHAR(100), nullable=False)
    descricao = Column(CHAR, nullable=False)
    valor_unitario = Column(Integer, unique=True, nullable=False)
    def __init__(self, id_produto, nome, descricao, valor_unitario):
        self.id_produto = id_produto
        self.nome = nome
        self.descricao = descricao
        self.valor_unitario = valor_unitario
        