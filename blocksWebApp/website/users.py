import os
import tornado.web
import tornado.ioloop
import asyncio
import logging 

from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
from jinja2 import Environment, FileSystemLoader

logging.basicConfig(
    filename="blocksWebServer2.log",
    level=logging.DEBUG,
    format= "%(levelname)s | %(asctime)s | %(threadName)s : %(message)s"
)

# Só funcionou quando a pasta templates ficou na blocksWebApp
TEMPLATES_DIRETORIA = os.path.join(os.path.dirname(os.path.dirname(__file__)), "templates")
jinja_environment = Environment(loader=FileSystemLoader(TEMPLATES_DIRETORIA))

class UsersHandler (tornado.web.RequestHandler):
    # Dicionário que pertence à classe
    listaUtilizadores = {
            "user1": ["funcionarioA","funcionarioB","funcionarioC"],
            "user2": ["funcionarioD","funcionarioF","funcionarioG"],
            "user3": ["funcionarioH","funcionarioI","funcionarioJ"]
    }

    def get(self, admin): #o admin pede uma lista de utilizadores da sua máquina maybe kinda   
        if admin in self.listaUtilizadores.keys():
            templateUsers = jinja_environment.get_template("users.html")
            self.write(templateUsers.render(lista_utilizadores = self.listaUtilizadores[admin], erros=[], msg="")) #AQUI PASSO POR ARGUMENTO OS FUNCIONARIOS
            
            logging.info("Os utilizadores do %s foram apresentados", admin)
        else:
            self.write({"erro": "Não é administrador"}) #devia e podia estar no template com jinja2

            logging.info("O utilizador %s não é admin", admin)