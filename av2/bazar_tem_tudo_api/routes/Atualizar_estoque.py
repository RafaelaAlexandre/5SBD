from flask import Blueprint, jsonify, request
from models import Produto, Movimentacao, db

atualizar_estoques_bp = Blueprint('atualizar_estoques', __name__)

@atualizar_estoques_bp.route('/atualizar_estoques', methods=['POST'])
def atualizar_estoque():
    data = request.json  # Assume que os dados são enviados como JSON

    if 'sku' not in data or 'quantidade' not in data:
        return jsonify({'error': 'Dados incompletos'}), 400

    sku = data['sku']
    quantidade = data['quantidade']

    produto = Produto.query.filter_by(sku=sku).first()

    if not produto:
        return jsonify({'error': 'Produto não encontrado'}), 404

    produto.estoque += quantidade
    db.session.add(produto)

    # Registra a movimentação de reposição
    nova_movimentacao = Movimentacao(sku=sku, quantidade=quantidade, status='comprado')
    db.session.add(nova_movimentacao)

    db.session.commit()

    return jsonify({'message': f'Estoque do produto {sku} atualizado com sucesso'}), 200

def configure_routes(app):
    app.register_blueprint(atualizar_estoques_bp)
