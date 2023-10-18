import os
from decouple import config

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

class Config:
    SECRET_KEY = config('SECRET_KEY','secret')
    DEBUG = config('DEBUG', cast=bool)
class Devconfig(Config):
    pass
class Qasconfig(Config):
    pass
class Prdconfig(Config):
    pass
config_dict = {
    'dev' : Devconfig,
    'qas' : Qasconfig,
    'prd' : Prdconfig,
}