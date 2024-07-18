from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Pedido(db.Model):
    id_pedido = db.Column(db.Integer, primary_key=True)
    valor_total = db.Column(db.Float, nullable=False)
    data_pedido = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(50), default='pendente')
    id_cliente = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
