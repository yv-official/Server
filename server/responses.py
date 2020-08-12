# response if Username Already Exist
from flask import jsonify,make_response
import json


# if user registered successfully 
def userRegistrationSuccessful(user, access_token, refresh_token):
    res = make_response(
            jsonify({
                'username': user.username,
                'msg': f"User with email {user.email} was created",
                'access_token': access_token,
                'refresh_token': refresh_token,
                'firstName': user.firstName,
                'lastName': user.lastName,
                'gender': user.gender,
                'phone': user.phone,
                'branch': user.branch,
                'year': user.year
            }),201 
        )
    return res

# response for Successful login
def userSuccessfulLogin(user, access_token, refresh_token):
    res = make_response(jsonify({
            'userId': str(user.id),
            'username': user.username,
            'firstName': user.firstName,
            'lastName': user.lastName,
            'msg': f"Logged in as {user.username}",
            'access_token': access_token,
            'refresh_token': refresh_token,
            'gender': user.gender,
            'phone': user.phone,
            'branch': user.branch,
            'year': user.year
        }),200)
    return res

# response for Authentication Failed
def authenticationFailed():
    res = make_response(
            jsonify({
                'msg': 'Authentication failed. Wrong Password'
                }),401
        )
    return res

def UserDoesNotExist():
    res = make_response(
            jsonify({
                'msg': 'No user found with that username'
                }),401
        )
    return res

def usernameAlreadyExist():
    res = make_response(
            jsonify({
                'msg': 'This Username is already taken!'
            }),401
        )
    return res

def emailAlreadyExist():
    res = make_response(
            jsonify({
                'msg': 'this email is already taken'
            }),401
        )
    return res

# response if something Went Wrong
def somethingWentWrong():
    res = make_response(
            jsonify({
                'msg': 'Something Went Wrong'
            }), 500 
        )
    return res

# response for refresh token revoke request
def refreshTokenRevoked():
    res = make_response(
            jsonify({
                'msg': 'refresh token has been Revoked'
                }),200
        )
    return res

# Response for access token revoke request
def accessTokenRevoked():
    res = make_response(
            jsonify({
                'msg': 'Access token has been Revoked'
                }),200
        )
    return res

# response for token refresh request
def tokenRefresh(user, access_token):
    res = make_response(jsonify({ 
                'username': user.username,
                'msg': f"Logged in as {user.email}",
                'access_token': access_token,
            }),200
        )
    return res
