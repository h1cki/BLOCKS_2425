import os
from jinja2 import Environment, FileSystemLoader
import tornado
import tornado.web
import logging

logging.basicConfig(
    filename="blocksWebServer2.log",
    level=logging.DEBUG,
    format= "%(levelname)s | %(asctime)s | %(threadName)s : %(message)s"
)

#só funcionou quando a pasta templates ficou na blocksWebApp
TEMPLATES_DIRETORIA = os.path.join(os.path.dirname(os.path.dirname(__file__)), "templates")
jinja_environment = Environment(loader=FileSystemLoader(TEMPLATES_DIRETORIA))

class LoginHandler (tornado.web.RequestHandler):
    def get (self):
        templateLogin = jinja_environment.get_template("login.html")
        self.write(templateLogin.render(erros=[], msg=""))
        
        logging.info('Página de Login acessada')
    
    def post(self):
        username = self.get_argument("email")
        password = self.get_argument("password")
        
        logging.info('POST RECEBEU USER: %s e PASS: %s', username, password)

        self.set_secure_cookie("user", tornado.escape.json_encode(username)) # de modo a guardar o user e poder aceder à personal page
        self.redirect("/personalpage")

#Não está feito
class LogoutHandler (tornado.web.RequestHandler):
    def get (self):
        self.write("LOGOUT")
        logging.info('Página de Logout acessada')

#Não está feito
class SignupHandler (tornado.web.RequestHandler):
    def get (self):
        self.write("SIGN-UP")
        logging.info('Página de Sign-up acessada')