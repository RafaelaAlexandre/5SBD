# routes/Receber_pedidos.py

from flask import Blueprint, jsonify, request, current_app
from models import db, Pedido, Item, Produto, Cliente
from datetime import datetime
import requests


receber_pedidos_bp = Blueprint('receber_pedidos', __name__)

@receber_pedidos_bp.route('/receber_pedido', methods=['POST'])
def receber_pedido():
    external_api_url = current_app.config['EXTERNAL_API_URL']

    # Fazendo a requisição à API externa
    response = requests.get(external_api_url)
    if response.status_code != 200:
        return jsonify({'message': 'Erro ao obter pedido da API externa.'}), 500

    data = response.json()

    # Verificar se todos os produtos do pedido estão registrados
    all_items_registered = all(Produto.query.filter_by(sku=item['sku']).first() for item in data['itens'])
    if not all_items_registered:
        return jsonify({'message': 'Um ou mais produtos no pedido não estão registrados.'}), 400

    # Verificar se o pedido já está registrado
    existing_pedido = Pedido.query.filter_by(id_pedido=data['id_pedido']).first()
    if existing_pedido:
        return jsonify({'message': 'Pedido já registrado.'}), 400

    # Verificar se o cliente já está registrado ou criar um novo cliente se não estiver
    existing_cliente = Cliente.query.filter_by(cpf=data['cpf']).first()
    if not existing_cliente:
        new_cliente = Cliente(
            nome_cliente=data['nome_cliente'],
            email=data['email'],
            cpf=data['cpf'],
            endereco=data['endereco']
        )
        db.session.add(new_cliente)
        db.session.commit()
        id_cliente = new_cliente.id
    else:
        id_cliente = existing_cliente.id

    # Registrar o pedido
    new_pedido = Pedido(
        valor_total=float(data['valor_total']),
        data_pedido=datetime.strptime(data['data_pedido'], '%Y-%m-%d').date(),
        status='pendente',
        id_cliente=id_cliente  # Certifique-se de que id_cliente é passado corretamente
    )
    db.session.add(new_pedido)
    db.session.commit()

    # Registrar os itens do pedido
    for item in data['itens']:
        new_item = Item(
            valor_itens=float(item['valor_itens']),
            quant=int(item['quant_produto']),
            id_pedido=new_pedido.id_pedido,  # Associar os itens ao pedido criado
            sku=item['sku']
        )
        db.session.add(new_item)

    db.session.commit()

    return jsonify({'message': 'Pedido recebido com sucesso.'}), 201
