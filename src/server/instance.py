from flask import Flask
from flask_restplus import Api

class Server():
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app,
            version='1.0',
            title='Consulta CNPJ parana',
            description="API criada com o objetivo de unificar consultas de CNPJ's em fontes publicas de dados",
            doc="/docs"
        )

    def run(self):
        self.app.run(
            debug=True
        )

server = Server()