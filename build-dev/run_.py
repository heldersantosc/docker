import logging
import http.server
import socketserver
import getpass 

class MyHTTPHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        logging.info("%s - - [%s] %s\n"%{
            self.client_address[0], 
            self.log_date_time_string(),
            format%args
        })

logging.basicConfig(
    filename='C:\\Users\\helder.santos\\Documents\\docker_new\\build-dev\\http-server',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logging.getLogger().addHandler(logging.StreamHandler())
logging.info('inicializando ....')
PORT = 8000

httpd = socketserver.TCPserver(("", PORT), MyHTTPHandler)
logging.info('escutando a porta: %s', PORT)
logging.info('usuario: %s', getpass.getuser())

httpd.server_forever()