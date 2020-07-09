import server.config as config
from flask import Flask
from flask_mongoengine import MongoEngine
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from server.settings import SECRET_KEY, JWT_SECRET_KEY, MONGO_URI, DB_NAME

app = Flask(__name__)

app.config['SECRET_KEY'] = SECRET_KEY
app.config['MONGODB_SETTINGS'] = {
    'host': MONGO_URI
}
app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']

cors = CORS(app, resources={r"/auth/*": {"origins": config.origins }})
jwt = JWTManager(app)
db = MongoEngine(app)


# Blueprint of API
from server.api import api
import server.routes

app.register_blueprint(api)

