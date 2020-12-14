import os
from config import *

def loadToken():
    if ENV_VARIABLE_NAME in os.environ:
        return os.environ['token']
    else:
        file = open(SECRET_FILE_NAME,"r")
        token = file.read()
        return token
