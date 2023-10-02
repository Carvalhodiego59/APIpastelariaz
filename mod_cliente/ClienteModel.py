import db
from sqlalchemy import Column, VARCHAR, CHAR, Integer
# ORM

class ClienteDB(db.Base):
    __tablename__ = 'tb_cliente'
    id_cliente = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nome = Column(VARCHAR(100), nullable=False)
    dia_fiado = Column(Integer, nullable=False)
    cpf = Column(CHAR(11), unique=True, nullable=False)
    telefone = Column(CHAR(11), nullable=False)
    compra_fiado = Column(Integer, nullable=False)
    senha = Column(VARCHAR(200), nullable=False)
    def __init__(self, id_cliente, nome, dia_fiado, cpf, telefone, compra_fiado, senha):
        self.id_funcionario = id_cliente
        self.nome = nome
        self.dia_fiado = dia_fiado
        self.cpf = cpf
        self.telefone = telefone
        self.compra_fiado = compra_fiado
        self.senha = senha