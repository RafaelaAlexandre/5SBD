# __init__db.py

from models import db, Produto

def init_db_data():
    # Produtos a serem inicializados
    produtos = [
        {'nome_produto': 'shampoo', 'sku': 'sku001', 'valor_produto': '20.00'},
        {'nome_produto': 'condicionador', 'sku': 'sku002', 'valor_produto': '25.00'},
        {'nome_produto': 'creme', 'sku': 'sku003', 'valor_produto': '10.00'},
        {'nome_produto': 'gel', 'sku': 'sku004', 'valor_produto': '15.00'},
        {'nome_produto': 'reparador', 'sku': 'sku005', 'valor_produto': '30.00'}
    ]

    # Inserindo produtos no banco de dados se ainda não existirem
    for produto in produtos:
        existing_produto = Produto.query.filter_by(sku=produto['sku']).first()
        if not existing_produto:
            new_produto = Produto(
                sku=produto['sku'],
                nome_produto=produto['nome_produto'],
                valor_produto=float(produto['valor_produto']),
                estoque=5  # valor inicial do estoque
            )
            db.session.add(new_produto)

    db.session.commit()

