class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///marketplace.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    EXTERNAL_API_URL = 'http://127.0.0.1:5001/pedido_aleatorio'  #api local que gera pedidos