import tornado
import tornado.web
import jinja2

from website.homepage import HomepageHandler
from website.auth import LoginHandler
from website.auth import LogoutHandler
from website.auth import SignupHandler
from website.personalPage import PersonalPageHandler
from website.users import UsersHandler
from website.dragDropFiles import POSTHandler
from website.dragDropFiles import BaseHandler

PORT = 8880

# Cria e retorna a aplicação Tornado com as rotas definidas
def make_app():
    handlers = [
        (r"/", HomepageHandler),  # Rota para a homepage
        (r"/login", LoginHandler), # Rota para a página de login
        (r"/logout", LogoutHandler), # Rota para a página de logout
        (r"/signup", SignupHandler), #Rota para a página de sign-up
        (r"/personalpage", PersonalPageHandler), #Rota para a página pessoal de um user
        (r"/users/(.*)", UsersHandler), # Rota que leva para a página onde estão os users da máquina
                                        # (.*) é o que faz poder receber users diferentes
        (r"/home/upload", BaseHandler), #Rota que permite ver o formulario de upload
        (r"/upload", POSTHandler), #Rota que permite carregar ficheiros 
    ]

    return tornado.web.Application(
        handlers,
        cookie_secret="hjscjadofdosfi",  # Aqui dentro da configuração da aplicação e é necessário para identificar o user
        port = PORT # de modo a ser possível ir mudando o valor da port 
    )