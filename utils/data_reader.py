import json
import os

def get_data(key):
    #Path setup
    path = os.path.join(os.path.dirname(__file__), "../data/users.json")
    with open(path) as file:
        data = json.load(file)
    return data[key]
