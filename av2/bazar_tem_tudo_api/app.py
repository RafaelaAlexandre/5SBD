# app.py

from flask import Flask
from config import Config
from models import db
from routes import configure_routes
from __init__db import init_db_data
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# Configuração do Swagger
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Bazar Tem Tudo API"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# Inicialização do banco de dados e dados iniciais
with app.app_context():
    db.create_all()
    init_db_data()

# Configuração das rotas
configure_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
