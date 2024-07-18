from flask import Blueprint, jsonify
from models import Compra

compras_db = Blueprint('compras', __name__)

@compras_db.route('/compras', methods=['GET'])
def get_compras():
    compras = Compra.query.all()
    return jsonify([{
        'id': compra.id,
        'sku': compra.sku,
        'quant': compra.quant
    } for compra in compras])

def configure_routes(app):
    app.register_blueprint(compras_db)
