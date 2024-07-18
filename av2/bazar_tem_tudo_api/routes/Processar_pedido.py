from flask import Blueprint, jsonify
from models import Pedido, Produto, Compra, db, Movimentacao, Item

processar_pedidos_bp = Blueprint('processar_pedidos', __name__)

@processar_pedidos_bp.route('/processar_pedidos', methods=['PUT'])
def processar_pedidos():
    pedidos = Pedido.query.order_by(Pedido.data_pedido).all()
    for pedido in pedidos:
        if pedido.status == 'pendente':
            itens = Item.query.filter_by(id_pedido=pedido.id_pedido).all()
            pode_atender = True
            for item in itens:
                produto = Produto.query.filter_by(sku=item.sku).first()
                if produto.estoque < item.quant:
                    pode_atender = False
                    falta_quantidade = item.quant - produto.estoque
                    # Registrar na tabela Compras
                    nova_compra = Compra(sku=item.sku, quant=falta_quantidade)
                    db.session.add(nova_compra)
                    db.session.commit()
                    break
            if pode_atender:
                for item in itens:
                    produto = Produto.query.filter_by(sku=item.sku).first()
                    produto.estoque -= item.quant
                    db.session.add(produto)

                    # Registra a movimentação de venda
                    nova_movimentacao = Movimentacao(sku=item.sku, quantidade=-item.quant, status='vendido')
                    db.session.add(nova_movimentacao)

                pedido.status = 'processado'
                db.session.add(pedido)
                db.session.commit()
    return jsonify({'message': 'Pedidos processados'})

def configure_routes(app):
    app.register_blueprint(processar_pedidos_bp)