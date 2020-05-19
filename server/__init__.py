from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a63c63e2bd1b7026d167905328720885'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['JWT_SECRET_KEY'] = '17cd18c1f2c822e8ee97'
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']
jwt = JWTManager(app)
db = SQLAlchemy(app)

# Blueprint of API
from server.api import api
import server.routes

app.register_blueprint(api)

