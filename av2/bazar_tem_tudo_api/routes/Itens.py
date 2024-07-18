from flask import Blueprint, jsonify
from models import Item

itens_bp = Blueprint('itens', __name__)

@itens_bp.route('/itens', methods=['GET'])
def get_itens():
    itens = Item.query.all()
    return jsonify([{
        'id_itens': item.id_itens,
        'valor_itens': item.valor_itens,
        'quant': item.quant,
        'id_pedido': item.id_pedido,
        'sku': item.sku
    } for item in itens])

def configure_routes(app):
    app.register_blueprint(itens_bp)