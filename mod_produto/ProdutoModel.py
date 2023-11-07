import db
from sqlalchemy import Column, VARCHAR, Integer, LargeBinary

# ORM


class ProdutoDB(db.Base):
    __tablename__ = "tb_produto"

    id_produto = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nome = Column(VARCHAR(100), nullable=False)
    descricao = Column(VARCHAR(100), nullable=True)
    foto = Column(LargeBinary, nullable=True)
    valor_unit = Column(Integer, nullable=False)

    def __init__(self, id_produto, nome, descricao, foto, valor_unit):
        self.id_produto = id_produto
        self.nome = nome
        self.descricao = descricao
        self.foto = foto
        self.valor_unit = valor_unit