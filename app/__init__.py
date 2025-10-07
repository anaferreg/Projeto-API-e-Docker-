from flask import Flask
from .models import db
from .routes import bp
from flasgger import Swagger

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///escola.db' 
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config['SWAGGER'] = {
        'title': 'API Escola',
        'uiversion': 3,
        'version': '1.0.0',
        'description': 'Uma API para gerenciar Alunos, Professores e Turmas.'
    }

    swagger = Swagger(app)

    app.register_blueprint(bp) 
    
    return app 