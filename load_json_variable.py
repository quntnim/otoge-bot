import json


def get_token():
    with open('./parameter.json') as f:
        data = json.load(f)
    return data['bot-token']
