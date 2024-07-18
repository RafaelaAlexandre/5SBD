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