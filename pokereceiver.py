# --------------------
#  poke-receiver file
# --------------------

import websocket as ws

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
        currRoom = ''
        for c in commands:
            parts = c.split("|")
            # if there are multiple commands on the same
            if (parts[0] != ''):
                currRoom = parts[0]
                continue
            commandQueue.append({
            'r' : currRoom,
            'c' : parts[1],
            'a' : parts[2:]
            })


    def login(self, user):
        # wait for receiving challstr
        if (user.username == '' or user.password == ''):
            return False




# some debugging stuff
if __name__ == '__main__':
    pkr = PokeReceiver()
    user = User()
