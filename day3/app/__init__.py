from flask import Flask
from flask_restx import Api
from .config.config import config_dict

def create_app(config=config_dict['dev']):
    try:
        app = Flask(__name__)
        app.config.from_object(config)
        
        api = Api(
            app,
            doc='/docs',
            title="Rest API Flask",
            description="Latihan membuat API dengan Flask"
        )
    except Exception as e:
        print("error : ", e)
    
    return app