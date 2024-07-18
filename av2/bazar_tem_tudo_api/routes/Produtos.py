from flask import Blueprint, jsonify
from models import Produto

produtos_db = Blueprint ('produtos',__name__)

@produtos_db.route('/produtos', methods=['GET'])
def get_produtos():
    produtos = Produto.query.all()
    return jsonify([{
        'sku': produto.sku,
        'nome_produto': produto.nome_produto,
        'valor_produto': produto.valor_produto,
        'estoque': produto.estoque
    } for produto in produtos])

def configure_routes(app):
    app.register_blueprint(produtos_db)