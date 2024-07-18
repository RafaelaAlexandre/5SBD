from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Models
class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_cliente = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    endereco = db.Column(db.String(200), nullable=False)

class Produto(db.Model):
    sku = db.Column(db.String(50), primary_key=True)
    nome_produto = db.Column(db.String(100), nullable=False)
    valor_produto = db.Column(db.Float, nullable=False)
    estoque = db.Column(db.Integer, default=5)

class Pedido(db.Model):
    id_pedido = db.Column(db.Integer, primary_key=True)
    valor_total = db.Column(db.Float, nullable=False)
    data_pedido = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(50), default='pendente')
    id_cliente = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)

class Item(db.Model):
    id_itens = db.Column(db.Integer, primary_key=True, autoincrement=True)
    valor_itens = db.Column(db.Float, nullable=False)
    quant = db.Column(db.Integer, nullable=False)
    id_pedido = db.Column(db.Integer, db.ForeignKey('pedido.id_pedido'), nullable=False)
    sku = db.Column(db.String(50), db.ForeignKey('produto.sku'), nullable=False)

class Compra(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.String(50), db.ForeignKey('produto.sku'), nullable=False)
    quant = db.Column(db.Integer, nullable=False)

class Movimentacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.String(50), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    data_movimentacao = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, sku, quantidade, status):
        self.sku = sku
        self.quantidade = quantidade
        self.status = status