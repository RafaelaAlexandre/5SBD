from .Clientes import configure_routes as configure_clientes_routes
from .Produtos import configure_routes as configure_produtos_routes
from .Pedidos import configure_routes as configure_pedidos_routes
from .Itens import configure_routes as configure_itens_routes
from .Compras import configure_routes as configure_compras_routes
from .Movimentacoes import configure_routes as configure_movimentacoes_routes
from .Atualizar_estoque import configure_routes as configure_atualizar_estoque_routes
from .Processar_pedido import configure_routes as configure_processar_pedidos_routes
from .Receber_pedidos import receber_pedidos_bp  # blueprint diretamente

def configure_routes(app):
    configure_clientes_routes(app)
    configure_produtos_routes(app)
    configure_pedidos_routes(app)
    configure_itens_routes(app)
    configure_compras_routes(app)
    configure_movimentacoes_routes(app)
    configure_atualizar_estoque_routes(app)
    configure_processar_pedidos_routes(app)
    app.register_blueprint(receber_pedidos_bp)  # Registrar a blueprint diretamente