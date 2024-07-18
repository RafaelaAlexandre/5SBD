from flask import Blueprint, jsonify
from models import Cliente

clientes_bp = Blueprint('clientes', __name__)

@clientes_bp.route('/clientes', methods=['GET'])
def get_clientes():
    clientes = Cliente.query.all()
    return jsonify([{
        'id': cliente.id,
        'nome_cliente': cliente.nome_cliente,
        'email': cliente.email,
        'cpf': cliente.cpf,
        'endereco': cliente.endereco
    } for cliente in clientes])

def configure_routes(app):
    app.register_blueprint(clientes_bp)
