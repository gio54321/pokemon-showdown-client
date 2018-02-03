import json

def getConfigData():
    # pretty self explanatory: loads the content of config.json
    parsed = ''
    try:
        with open('config.json', 'r') as conf:
            parsed = json.loads(conf.read())
    except FileNotFoundError as e:
        print('You have to create a config.json to use poke-client')

    return parsed

# actually some debuggin stuff
if (__name__ == '__main__'):
    print(getConfigData())
