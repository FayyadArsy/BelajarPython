from flask import Flask
from flask_restx import Api
from .config.config import config_dict
from .views.users import users_ns

def create_app(config=config_dict['dev']):
    app = Flask(__name__)
    app.config.from_object(config)
    
    api = Api(
        app,
        doc='/docs',
        title="Rest API Flask",
        description="Latihan membuat API dengan Flask"
    )

    api.add_namespace(users_ns)
    
    return app