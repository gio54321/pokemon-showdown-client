
from pokeconfig import *

class User:
    def __init__(self):
        config = getConfigData()
        self.username = config.get('username')
        self.password = config.get('password')

        # check if the user has actually changed credentials in config.json
        if (self.username == '' or self.password == ''):
            print('you have to change username password in config.json')

if __name__ == '__main__':
    user = User()
