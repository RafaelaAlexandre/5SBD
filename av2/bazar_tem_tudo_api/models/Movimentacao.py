from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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