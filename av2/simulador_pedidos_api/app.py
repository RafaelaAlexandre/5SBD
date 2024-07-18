from flask import Flask, jsonify
from datetime import datetime
import random

app = Flask(__name__)

# Lista de produtos predefinidos
produtos = [
    {'nome_produto': 'shampoo', 'sku': 'sku001', 'valor_produto': '20.00'},
    {'nome_produto': 'condicionador', 'sku': 'sku002', 'valor_produto': '25.00'},
    {'nome_produto': 'creme', 'sku': 'sku003', 'valor_produto': '10.00'},
    {'nome_produto': 'gel', 'sku': 'sku004', 'valor_produto': '15.00'},
    {'nome_produto': 'reparador', 'sku': 'sku005', 'valor_produto': '30.00'}
]

# Lista de nomes de clientes para exemplo
nomes_clientes = ['Ana Silva', 'Bruno Souza', 'Carlos Almeida', 'Daniela Ramos', 'Eduardo Lima']

# Lista global para armazenar pedidos
pedidos = []


# Função para criar um item de pedido aleatório
def criar_item(id_item, produtos_especificos=True):
    if produtos_especificos:
        produto = random.choice(produtos)
    else:
        produto = {
            'nome_produto': f'produto_{random.randint(1, 100)}',
            'sku': f'sku_{random.randint(1, 100)}',
            'valor_produto': f'{random.uniform(10, 100):.2f}'
        }
    quantidade = random.randint(1, 5)
    valor_item = float(produto['valor_produto']) * quantidade
    return {
        'id_itens': id_item,
        'sku': produto['sku'],
        'nome_produto': produto['nome_produto'],
        'valor_produto': produto['valor_produto'],
        'quant_produto': quantidade,
        'valor_itens': f'{valor_item:.2f}'
    }


# Função para criar um pedido aleatório
def criar_pedido(id_pedido, produtos_especificos=True):
    nome_cliente = random.choice(nomes_clientes)
    email = nome_cliente.lower().replace(' ', '.') + '@example.com'
    cpf = f'{random.randint(100, 999)}.{random.randint(100, 999)}.{random.randint(100, 999)}-{random.randint(10, 99)}'
    endereco = f'Rua {random.choice(["das Flores", "da Paz", "das Acácias", "Paulista", "Brasil"])}, {random.randint(1, 1000)}, {random.choice(["São Paulo, SP", "Rio de Janeiro, RJ", "Belo Horizonte, MG", "Curitiba, PR"])}'
    itens = [criar_item(i, produtos_especificos) for i in range(1, random.randint(2, 5))]
    valor_total = sum(float(item['valor_itens']) for item in itens)
    return {
        'nome_cliente': nome_cliente,
        'email': email,
        'cpf': cpf,
        'endereco': endereco,
        'id_pedido': id_pedido,
        'valor_total': f'{valor_total:.2f}',
        'data_pedido': datetime.now().strftime('%Y-%m-%d'),
        'itens': itens
    }


# Inicializar a lista de pedidos
def inicializar_pedidos():
    global pedidos
    for id_pedido in range(1, 101):
        if id_pedido <= 50:
            # Criar pedidos com produtos especificados
            pedido = criar_pedido(id_pedido, produtos_especificos=True)
        else:
            # Criar pedidos com produtos variados
            pedido = criar_pedido(id_pedido, produtos_especificos=False)

        pedidos.append(pedido)


# Inicializar os pedidos ao iniciar o servidor
inicializar_pedidos()


# Rota para obter um pedido aleatório
@app.route('/pedido_aleatorio', methods=['GET'])
def pedido_aleatorio():
    pedido = random.choice(pedidos)
    return jsonify(pedido)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
