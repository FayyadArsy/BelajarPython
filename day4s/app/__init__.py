from flask import Flask
from flask_restx import Api
from flask_migrate import Migrate
from .config.config import config_dict
from .views.users import users_ns
from .utils import db
from .models import users

def app_tugas(config=config_dict['dev']):
    app = Flask(__name__)
    app.config.from_object(config)

    fb.init_app(app)
    api = Api(
        app,
        doc='/docs',
        title='Tugas Api Flask',
        description="Tugas Individu membuat API dengan Flask"
    )

api.add_namespace(users_ns)
migerate = Migrate(app, db)
return app