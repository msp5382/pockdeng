import threading
from PockDengServer import startServer
import socket
from WebServ.PockDengWebService import Webserver

t1 = threading.Thread(target=Webserver)
t1.daemon = True 

def app():
    isMultiplayer = 'yes'
    t1.start()
    if (isMultiplayer == 'yes' or isMultiplayer == 'Yes' or isMultiplayer == 'Y' or isMultiplayer == 'y'):
        isStartServer = input('Start Pockdeng server? (Yes/No) : ')
        if (isStartServer == 'yes' or isStartServer == 'Yes' or isStartServer == 'Y' or isStartServer == 'y'):
            print('Server started')
            pockdengIP = [l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [
                                      [(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0]
            print('Server IP address :', pockdengIP, "port : 3500")
            startServer()
        else:
            while True:
                pass
app()