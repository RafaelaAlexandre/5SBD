from flask import Blueprint, jsonify
from models import Pedido, Cliente

pedidos_db = Blueprint('pedidos', __name__)

@pedidos_db.route('/pedidos', methods=['GET'])
def get_pedidos():
    pedidos = Pedido.query.all()
    return jsonify([{
        'id_pedido': pedido.id_pedido,
        'valor_total': pedido.valor_total,
        'data_pedido': pedido.data_pedido.strftime('%Y-%m-%d'),
        'status': pedido.status,
        'id_clientes': pedido.id_cliente
    } for pedido in pedidos])

def configure_routes(app):
    app.register_blueprint(pedidos_db)
