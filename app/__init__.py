from flask import Flask, app
from config import config_options,DevConfig
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_name):
    app=Flask(__name__)
    
     #Creating the main configurations
    app.config.from_object(config_options[config_name])
    
   # initializing flask extentions
    db.init_app(app)
    
     # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app
