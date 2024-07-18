from flask import Blueprint, jsonify
from models import Movimentacao

movimentacoes_bp = Blueprint('movimentacoes', __name__)

@movimentacoes_bp.route('/movimentacoes', methods=['GET'])
def get_movimentacoes():
    movimentacoes = Movimentacao.query.all()
    return jsonify([{
        'id': movimentacao.id,
        'sku': movimentacao.sku,
        'quantidade': movimentacao.quantidade,
        'status': movimentacao.status,
        'data_movimentacao': movimentacao.data_movimentacao.strftime('%Y-%m-%d %H:%M:%S')
    } for movimentacao in movimentacoes])


def configure_routes(app):
    app.register_blueprint(movimentacoes_bp)