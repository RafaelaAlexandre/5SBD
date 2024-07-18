from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Produto(db.Model):
    sku = db.Column(db.String(50), primary_key=True)
    nome_produto = db.Column(db.String(100), nullable=False)
    valor_produto = db.Column(db.Float, nullable=False)
    estoque = db.Column(db.Integer, default=5)