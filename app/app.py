# app.py (ou seu arquivo principal)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger  # 1. Importe o Swagger
from routes import bp

# Configuração do App e do Banco de Dados
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///escola.db' # config pressupondo que o db estera na mesma pasta
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# 2. Configure e inicialize o Swagger
app.config['SWAGGER'] = {
    'title': 'API Escola',
    'uiversion': 3,
    'version': '1.0.0',
    'description': 'Uma API para gerenciar Alunos, Professores e Turmas.'
}
swagger = Swagger(app)

# Registro do Blueprint
app.register_blueprint(bp)

if __name__ == '__main__':
    app.run(debug=True)