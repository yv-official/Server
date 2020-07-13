from flask import Blueprint

import server.helpers as helpers
import server.Models.users as users
import server.exceptions as exceptions
import server.responses as responses

from flask_jwt_extended import jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt,create_access_token, create_refresh_token
from datetime import datetime, timedelta

# Create blue print for API
api = Blueprint('api', 'api', url_prefix='/api')


# function for registration
def register():
    data = helpers.register_parser().parse_args()
    username = data['username']
    email = data['email']
    password = users.generate_hash(data['password'])
    firstName = data['firstName']
    lastName = data['lastName']
    gender = data['gender']
    phone = data['phone']
    branch = data['branch']
    year = data['year']

    # try to Create User of the given information
    try:
        user = helpers.userRegister(username, email, password, firstName, lastName, gender, phone, branch, year)
        
        # Add entry in DATABASE 
        user.save()

        # access_token
        access_token = create_access_token(identity=user.email, expires_delta=timedelta(days=1))
        # refresh_token
        refresh_token = create_refresh_token(identity = user.email)
        
        return responses.userRegistrationSuccessful(user, access_token, refresh_token)

    except exceptions.UsernameAlreadyExist:
        return responses.usernameAlreadyExist()

    except exceptions.EmailAlreadyExist:
        return responses.emailAlreadyExist()

# function for login
def login():
    data = helpers.login_parser().parse_args()
    username = data['username']
    password = data['password']

    try:
        user = helpers.userLogin(username, password)
    
        # access token
        access_token = create_access_token(identity=user.email, expires_delta=timedelta(days=1))
        #refresh token
        refresh_token = create_refresh_token(identity = user.email)

        return responses.userSuccessfulLogin(user, access_token, refresh_token)
    
    except exceptions.AuthenticationFailed:
        return responses.authenticationFailed()
    except exceptions.UserDoesNotExist:
        return responses.UserDoesNotExist()


# function to revoke Access Token
@jwt_required
def logoutAccess():
    jti = get_raw_jwt()['jti']
    
    try:
        helpers.userLogoutAccessToken(jti)
        return responses.accessTokenRevoked()
    
    except exceptions.SomethingWentWrong:
        return responses.somethingWentWrong()

# function to revoke Refresh Token
@jwt_refresh_token_required
def logoutRefresh():
    jti = get_raw_jwt()['jti']
    try:
        helpers.userLogoutRefreshToken(jti)
        return responses.refreshTokenRevoked()
    
    except exceptions.SomethingWentWrong:
        return responses.somethingWentWrong()

# function to refresh the token
@jwt_refresh_token_required
def tokenRefresh():
    email = get_jwt_identity()
    try:
        user = helpers.tokenRefresh(email)
        access_token = create_access_token(identity = user.email, expires_delta=timedelta(days=1))
        return responses.tokenRefresh(user, access_token)
    
    except exceptions.AuthenticationFailed:
        return responses.authenticationFailed()


