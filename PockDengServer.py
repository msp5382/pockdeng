from http.server import BaseHTTPRequestHandler, HTTPServer
import random
import json

from PockDengValidator import validate,getNum

from PockDengDatabase import saveRoom,readRoom,saveJao,readJao,clearJao

clearJao()

def parse_qs(replacer, url):
    res = {}
    url = url.replace('/' + replacer + '?', '')
    param = url.split('&')
    for i in param:
        res[i.split('=')[0]]=i.split('=')[1]
    return res



users = {}

cards = ["A", "2", "3", "4", "5", "6", "7","8", "9", "10", "J", "Q", "K"]

char = ['C', 'D', 'H', 'S']

def getScore(c):
    score = 0
    if (9 > cards.index(c)):
        score = cards.index(c) + 1
    else:
        score = 0
    return score

def joinRoom(userjson):
    print(userjson)
    users[userjson['username']] = userjson['put']
    saveRoom(users)
    return {'status': 'ok'}


def getCard():
    selected1 = cards[random.randint(0, len(cards) - 1)]
    selected2 = cards[random.randint(0, len(cards) - 1)]
    score = getScore(selected1)+getScore(selected2)
    return {'status': 'ok', '1card': selected1+char[random.randint(0,3)], '2card': selected2+char[random.randint(0,3)], 'score':score}


def drawCard():
    selected = cards[random.randint(0, len(cards) - 1)]
    score = getScore(selected)
    return {'status': 'ok', 'drawcard': selected+char[random.randint(0,3)],'score':score}



JaoTam = [getCard()['1card'],getCard()['2card']]

#print("JAOMUE DAI : ",JaoTam)

def placeCard(cardJSON):
    # format
    # { user: name , score : score }
    bag.append(cardJSON)
    return {'status': 'ok'}

def getWinner():
    return {'status': 'ok', 'bag': bag}

def getUser():
    return readRoom()

def finalScore(cards):
    _cards = cards['cards'].split(',')
    print(validate(_cards,JaoTam))
    return validate(_cards,JaoTam)

bag = []

def getJao():
    return readJao()

def editScore(userjson):
    print(userjson)
    users[userjson['username']] = userjson['edit']
    saveRoom(users)
    return {'status': 'ok'}

def editJao(point):
    jao = readJao()
    jao += int(point['edit'])
    saveJao(jao)
    return {'status': 'ok'}

class S(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        pass
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        if 'join' in self.path:
            self.wfile.write(bytes(json.dumps(joinRoom(parse_qs('join',self.path))), 'utf-8'))
        elif 'getcard' in self.path:
            self.wfile.write(bytes(json.dumps(getCard()), 'utf-8'))
        elif 'drawcard' in self.path:
            self.wfile.write(bytes(json.dumps(drawCard()), 'utf-8'))
        elif 'getwinner' in self.path:
            self.wfile.write(bytes(json.dumps(getWinner()), 'utf-8'))
        elif 'placecard' in self.path:
            self.wfile.write(bytes(json.dumps(placeCard(parse_qs(self.path[2:]))), 'utf-8'))
        elif 'usersync' in self.path:
            self.wfile.write(bytes(json.dumps(getUser()), 'utf-8'))
        elif 'getscore' in self.path:
            self.wfile.write(bytes(json.dumps(finalScore(parse_qs('getscore', self.path))), 'utf-8'))
        elif 'getjao' in self.path:
            self.wfile.write(bytes(json.dumps(getJao()), 'utf-8'))
        elif 'editscore' in self.path:
            self.wfile.write(bytes(json.dumps(editScore(parse_qs('editscore', self.path))), 'utf-8'))
        elif 'editjao' in self.path:
            self.wfile.write(bytes(json.dumps(editJao(parse_qs('editjao',self.path))), 'utf-8'))
            # /getscore?cards=1H,2H,3H//


    def do_HEAD(self):
        self._set_headers()


def startServer(server_class=HTTPServer, handler_class=S, port=3500):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting Pockdeng Server on 3500')
    httpd.serve_forever()
    

    #AI JaoMue
    

