from flask import Flask
from flask_restx import Api
from flask_migrate import Migrate
# from flask_sqlalchemy import SQLAlchemy
from .config.config import config_dict
from .views.users import users_ns
from .utils import db
from .models import users
from .models import blogs

def create_app(config=config_dict['dev']):
    app = Flask(__name__)
    app.config.from_object(config)
    
    db.init_app(app)
    api = Api(
        app,
        doc='/docs',
        title="Rest API Flask",
        description="Latihan membuat API dengan Flask"
    )

    api.add_namespace(users_ns)
    # api.add_namespace(users_ns)
    migrate = Migrate(app, db)
    return app