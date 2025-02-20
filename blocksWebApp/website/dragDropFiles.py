import os
import asyncio
import logging
import tornado
from tornado import options
from jinja2 import Environment, FileSystemLoader

logging.basicConfig(
    filename="blocksWebServer.log",
    level=logging.DEBUG,
    format= "%(levelname)s | %(asctime)s | %(threadName)s : %(message)s"
)

# Só funcionou quando a pasta templates ficou na blocksWebApp
TEMPLATES_DIRETORIA = os.path.join(os.path.dirname(os.path.dirname(__file__)), "templates")
jinja_environment = Environment(loader=FileSystemLoader(TEMPLATES_DIRETORIA))

UPLOAD_DIR = "UploadsDoSite"  # Diretório onde os arquivos serão armazenados
os.makedirs(UPLOAD_DIR, exist_ok=True)  # Criar a pasta se não existir

class BaseHandler (tornado.web.RequestHandler):
    def get(self):
        port = self.application.settings["port"]
        templateUpload = jinja_environment.get_template("blocksServerTemplate.html")
        self.write(templateUpload.render(erros=[], msg="", port_actual=port)) # Tem o HTML e javascript que permite o drag-and-drop

class POSTHandler(tornado.web.RequestHandler):
    def post(self):
        for field_name, files in self.request.files.items():
            for info in files:
                filename, content_type = info["filename"], info["content_type"]                    
                body = info["body"]

                filepath = os.path.join(UPLOAD_DIR, filename)  # Caminho onde guardar
                
                with open(filepath, "wb") as f:
                    f.write(body)  # Guarda o ficheiro

                logging.info('POST "%s" "%s" %d bytes', filename, content_type, len(body))
                logging.info(f'POST "{filename}" saved at {filepath}')

# @jondinham no stackoverflow
# Dá para recuperar os ficheiros através do site
class GETHandler (tornado.web.RequestHandler):
    def get(self, filename):
        filepath = os.path.join(UPLOAD_DIR, filename)  # Certificar que lê da pasta correta

        if not os.path.exists(filepath):
            self.set_status(404)
            self.write("File not found")
            return

        with open(filepath, "r") as file:
            self.write(file.read())

        logging.info("Get request made to retreive file")
        logging.info(f"GET request made to retrieve file: {filepath}")
