# response if Username Already Exist
from flask import jsonify,make_response
import json

from flask_jwt_extended import (
    set_access_cookies,
    set_refresh_cookies,
    unset_jwt_cookies
)


one_day = 60*60*24
thirty_days = 60*60*24*30

# if user registered successfully 
def userRegistrationSuccessful(user):
    res = make_response(
            jsonify({
                'username': user.username,
                'msg': f"User with email {user.email} was created",
            }),201 
        )
    return res

# response for Successful login
def userSuccessfulLogin(user, access_token, refresh_token, rememberMe):
    res = jsonify({
            "info":{
                'userId': str(user.id),
                'username': user.username,
                'firstName': user.firstName,
                'lastName': user.lastName,
                'msg': f"Logged in as {user.username}",
                'gender': user.gender,
                'phone': user.phone,
                'branch': user.branch,
                'year': user.year,
            },
            "about": user.about.to_mongo(),
            "privacy": user.settings.to_mongo()
        })
    set_access_cookies(res, access_token, max_age=one_day)
    # print(type(rememberMe))
    # print(rememberMe == "True")
    if rememberMe == "True":
        set_refresh_cookies(res, refresh_token, max_age=thirty_days)
    else:
        set_refresh_cookies(res, refresh_token, max_age=one_day)
    return make_response(res,200)

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

def noTokenFound():
    res = make_response(
        jsonify({
            'msg': 'No token found'
        }), 301
    )
    return res

# response to logout user
def logoutUser():
    res = jsonify({
        'msg':"User logged out"
    })
    unset_jwt_cookies(res)
    return make_response(res,200)


# response for token refresh request
def tokenRefresh(user, access_token):
    res = jsonify({ 
            "info":{
                'userId': str(user.id),
                'username': user.username,
                'firstName': user.firstName,
                'lastName': user.lastName,
                'msg': f"Logged in as {user.username}",
                'gender': user.gender,
                'phone': user.phone,
                'branch': user.branch,
                'year': user.year
                },
            "about": user.about.to_mongo(),
            "privacy": user.settings.to_mongo()
            })
    set_access_cookies(res, access_token, max_age=one_day)
    return make_response(res,200)

def userDetailsUpdated(user):
    res = jsonify({
        "about": user.about.to_mongo(),
        "privacy": user.settings.to_mongo()
    })
    return make_response(res,200)
