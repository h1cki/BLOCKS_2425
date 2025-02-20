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

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        user = self.get_secure_cookie("user")
        return user.decode() if user else None

class PersonalPageHandler (BaseHandler):
    def get (self): 
        username = self.get_current_user() # costuma vir com "" e não devia
        if username.startswith('"') and username.endswith('"'):
            username = username.strip('"')

        logging.info('Página Pessoal acessada por %s',username)
        
        templateLogin = jinja_environment.get_template("personalPage.html")
        self.write(templateLogin.render(erros=[], msg="", user_name=username)) #AQUI PASSO POR ARGUMENTO O USER
        
        logging.info('Página Pessoal acessada por %s e o template apareceu',username)