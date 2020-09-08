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

# only allow JWT cookies to be sent over https. In PRODUCTION, this should likely be True
app.config['JWT_COOKIE_SECURE'] = False

# configure application to store JWTs in cookies
app.config['JWT_TOKEN_LOCATION'] = ['cookies']

# set cookie path so that your are only sending your access token cookies to the access endpoint, and only sending your refresh token to the refresh endpoint.
# app.config['JWT_ACCESS_COOKIE_PATH'] = '/api/'
# app.config['JWT_REFRESH_COOKIE_PATH'] = 'api/token/refresh'

# enable CSRF double submit protection
app.config['JWT_COOKIE_CSRF_PROTECT'] = True

# By default, the CRSF cookies will be called csrf_access_token and
# csrf_refresh_token, and in protected endpoints we will look for the
# CSRF token in the 'X-CSRF-TOKEN' header.


app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']



cors = CORS(app, resources={r"/api/*": {"origins": config.origins, "supports_credentials": True }})
jwt = JWTManager(app)
db = MongoEngine(app)


# Blueprint of API
from server.api import api
import server.routes

app.register_blueprint(api)

