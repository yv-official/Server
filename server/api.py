from flask import Blueprint

import server.helpers as helpers
import server.Models.users as users
import server.exceptions as exceptions
import server.responses as responses

from flask_jwt_extended import jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt,create_access_token, create_refresh_token
from datetime import datetime, timedelta

import ast

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
        return responses.userRegistrationSuccessful(user)

    except exceptions.UsernameAlreadyExist:
        return responses.usernameAlreadyExist()

    except exceptions.EmailAlreadyExist:
        return responses.emailAlreadyExist()

# function for login
def login():
    data = helpers.login_parser().parse_args()
    username = data['username']
    password = data['password']
    rememberMe = data['rememberMe']
    # print(username, password, rememberMe)
    try:
        user = helpers.userLogin(username, password)
    
        # access token
        access_token = create_access_token(identity=user.email, expires_delta=timedelta(days=1))
        #refresh token
        # print(rememberMe == "True")
        if rememberMe == "True":
            refresh_token = create_refresh_token(identity = user.email)
        else:
            refresh_token = create_refresh_token(identity = user.email, expires_delta=timedelta(days=1))

        return responses.userSuccessfulLogin(user, access_token, refresh_token, rememberMe)
    
    except exceptions.AuthenticationFailed:
        return responses.authenticationFailed()
    except exceptions.UserDoesNotExist:
        return responses.UserDoesNotExist()


# function to blacklist Access Token
# @jwt_required
# def logoutAccess():
#     jti = get_raw_jwt()['jti']
    
#     try:
#         helpers.userLogoutAccessToken(jti)
#         return responses.accessTokenRevoked()
    
#     except exceptions.SomethingWentWrong:
#         return responses.somethingWentWrong()

    
# backend will send us a repsonse with unsetted cookies in order to logout
@jwt_refresh_token_required
def logout():
    jti = get_raw_jwt()['jti']
    try:
        # will blacklist current refresh token
        helpers.userLogoutRefreshToken(jti)
        return responses.logoutUser()
    
    except exceptions.SomethingWentWrong:
        return responses.somethingWentWrong()

# function to refresh the token
@jwt_refresh_token_required
def tokenRefresh():
    email = get_jwt_identity()
    print(email)
    try:
        user = helpers.tokenRefresh(email)
        access_token = create_access_token(identity = user.email, expires_delta=timedelta(days=1))
        return responses.tokenRefresh(user, access_token)
    
    except exceptions.NoTokenFound:
        return responses.noTokenFound()

# function updating user details
@jwt_required
def updateDetails():
    data = helpers.update_parser().parse_args()
    newData = data['data']
    newPrivacy = data['privacy']

    newData = ast.literal_eval(newData)
    newPrivacy =  ast.literal_eval(newPrivacy)
    
    current_user_email = get_jwt_identity()

    try:
        user = helpers.updateUserDetails(current_user_email, newData, newPrivacy)
        user.save()
        return responses.userDetailsUpdated(user)
    except exceptions.SomethingWentWrong:
        return response.somethingWentWrong()


    



