# --------------------
#  poke-receiver file
# --------------------

import websocket as ws
import request

from user import *
from pokeconfig import *

class PokeReceiver:
    def __init__(self):
        # get content of config.json
        self.config = getConfigData()
        #create the main websocket connection
        self.socket = ws.create_connection(self.config['socketServer'])
        self.commandQueue = []

    def receiveData(self):
        # get data from server
        data = self.socket.recv()

        # each line represent a command
        commands = data.split('\n')
        print (commands)
        currRoom = ''
        for c in commands:
            parts = c.split("|")
            # if there are multiple commands on the same
            if (parts[0] != ''):
                currRoom = parts[0]
                continue
            self.commandQueue.append({
            'r' : currRoom,
            'c' : parts[1],
            'a' : parts[2:]
            })


    def login(self, user):
        # check if the credentials has been changed in config.json
        if (user.username == '' or user.password == ''):
            return False

        # receive data until he receive challstr
        challstr = ''
        while challstr == '':
            self.receiveData()
            for c in self.commandQueue:
                if (c['c'] == 'challstr'):
                    challstr = c['a'][0] + '|' + c['a'][1]

        print('challstr: ' + challstr)

        # request data from authserver to get assertion
        data = {
            'act' : 'login',
            'name' : user.username,
            'pass' : user.password,
            'challstr' : challstr
        }
        r = request.post(self.config['actionServer'], data)
        response = json.loads(r.text[1:])


# some debugging stuff
if __name__ == '__main__':
    pkr = PokeReceiver()
    user = User()
    pkr.login(user)
