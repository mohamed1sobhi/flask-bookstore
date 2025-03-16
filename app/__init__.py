from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect 
from config import config

bootstrap = Bootstrap5()
db = SQLAlchemy()
migrate = Migrate()


def create_app(environment):
    app = Flask(__name__)
    app.config.from_object(config.get(environment or 'development'))
    db.init_app(app)
    bootstrap.init_app(app)

    from . import models
    migrate.init_app(app,db)

    register_blueprints(app)
    return app

def register_blueprints(application):
    from app.main.routes import main_blueprint
    from app.auth.routes import auth_blueprint

    application.register_blueprint(main_blueprint)
    application.register_blueprint(auth_blueprint)