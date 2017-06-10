import os
from flask import Flask, render_template, request, redirect
from .models import db
from flask_migrate import Migrate

BASE_DIR = os.path.dirname(os.path.abspath(__name__))
database = os.path.join(BASE_DIR, 'database.db')
app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(database)
app.config["SECRET_KEY"] = "hello"

migrate = Migrate(app, db)

db.init_app(app)
    
def create_tables():
    with app.app_context():
        db.create_all()

from .views import *