import os, sys
from .config import *

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

def loadToken():
    if ENV_VARIABLE_NAME in os.environ:
        return os.environ['token']
    else:
        file = open(os.path.join(__location__, SECRET_FILE_NAME),"r")
        token = file.read()
        return token
