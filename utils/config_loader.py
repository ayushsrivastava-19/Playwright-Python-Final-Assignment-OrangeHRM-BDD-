import configparser
import os

def get_config(section, key):
    config = configparser.ConfigParser()
    path = os.path.join(os.path.dirname(__file__), '../config/config.ini')
    config.read(path)
    return config.get(section, key)