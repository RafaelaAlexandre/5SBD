from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Item(db.Model):
    id_itens = db.Column(db.Integer, primary_key=True, autoincrement=True)
    valor_itens = db.Column(db.Float, nullable=False)
    quant = db.Column(db.Integer, nullable=False)
    id_pedido = db.Column(db.Integer, db.ForeignKey('pedido.id_pedido'), nullable=False)
    sku = db.Column(db.String(50), db.ForeignKey('produto.sku'), nullable=False)