from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Compra(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.String(50), db.ForeignKey('produto.sku'), nullable=False)
    quant = db.Column(db.Integer, nullable=False)
