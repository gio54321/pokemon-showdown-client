# -------------------------------------
#  main file of the poke-client module
# -------------------------------------

from poke-receiver import *

class PokeClient:
    def __init__(self, **options):

        # enable debug if there is the flag debug=True
        self.debug = False
        if options.get('debug'): self.debug = True

        if self.debug: print('Initializing the PokeClient object')

        self.receiver = PokeReceiver()
        
