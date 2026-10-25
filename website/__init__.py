from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__) #__name__ is the name of current module aka ("website") in this case, Flask used it to find templates & static folders
    app.config['SECRET_KEY'] = 'just type random thing'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views #import the blueprint it means
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note #to make sure the stuffs in models are being defined before we make anything

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login' #essentially where should flask redirect us if user isnt logged in and it says login required
    login_manager.init_app(app)

    @login_manager.user_loader #this declaration is telling flask to use the func below to load user
    def load_user(id):
        return User.query.get(int(id)) #telling flask how we load auser (similar to filter by but looking at primary key)

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME): #to determine wheter a database alr exists
        with app.app_context():
            db.create_all()
        print('Created Database!')