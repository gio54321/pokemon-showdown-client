# --------------------
#  poke-receiver file
# --------------------

import websocket as ws

from pokeconfig import *

class PokeReceiver:
    def __init__(self):
        # get content of config.json
        self.config = getConfigData()
        #create the main websocket connection
        self.socket = ws.create_connection(self.config['socketServer'])

    def login(self, user):
        


# some debugging stuff
if __name__ == '__main__':
    pkr = PokeReceiver()
