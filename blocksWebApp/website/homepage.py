import os
import tornado
import tornado.web
import logging
from jinja2 import Environment, FileSystemLoader

logging.basicConfig(
    filename="blocksWebServer2.log",
    level=logging.DEBUG,
    format= "%(levelname)s | %(asctime)s | %(threadName)s : %(message)s"
)

#só funcionou quando a pasta templates ficou na blocksWebApp
TEMPLATES_DIRETORIA = os.path.join(os.path.dirname(os.path.dirname(__file__)), "templates")
jinja_environment = Environment(loader=FileSystemLoader(TEMPLATES_DIRETORIA))

class HomepageHandler (tornado.web.RequestHandler):
    def get (self):
        templateHome = jinja_environment.get_template("homepage.html")
        self.write(templateHome.render(erros=[], msg=""))
        
        logging.info('Acesso bem executado')