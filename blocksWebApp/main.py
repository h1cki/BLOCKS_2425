import os
import tornado
from tornado import options
import asyncio
from jinja2 import Environment, FileSystemLoader
from website import make_app
import logging

logging.basicConfig(
    filename="blocksWebServer2.log",
    level=logging.DEBUG,
    format= "%(levelname)s | %(asctime)s | %(threadName)s : %(message)s"
)

async def main():
    options.parse_command_line()
    app = make_app()
    port = app.settings["port"]
    app.listen(port)
    print("Servidor iniciado na porta", port)
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())