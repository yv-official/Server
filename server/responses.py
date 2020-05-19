# response if Username Already Exist
from flask import jsonify,make_response


# if user registered successfully 
def userRegistrationSuccessful(user, access_token, refresh_token):
    res = make_response(
            jsonify({
                'username': user.username,
                'message': f"User with email {user.email} was created",
                'access_token': access_token,
                'refresh_token': refresh_token
            }),201 
        )
    return res

# response for Successful login
def userSuccessfulLogin(user, access_token, refresh_token):
    res = make_response(jsonify({
            'username': user.username,
            'message': f"Logged in as {user.email}",
            'access_token': access_token,
            'refresh_token': refresh_token,
        }),200)
    return res

# response for Authentication Failed
def authenticationFailed():
    res = make_response(
            jsonify({
                'error': 'Authentication failed'
                }),401
        )
    return res

def usernameAlreadyExist():
    res = make_response(
            jsonify({
                'error': 'This Username is already taken!'
            }),401
        )
    return res

def emailAlreadyExist():
    res = make_response(
            jsonify({
                'error': 'this email is already taken'
            }),401
        )
    return res

# response if something Went Wrong
def somethingWentWrong():
    res = make_response(
            jsonify({
                'error': 'Something Went Wrong'
            }), 500 
        )
    return res

# response for refresh token revoke request
def refreshTokenRevoked():
    res = make_response(
            jsonify({
                'message': 'refresh token has been Revoked'
                }),200
        )
    return res

# Response for access token revoke request
def accessTokenRevoked():
    res = make_response(
            jsonify({
                'message': 'Access token has been Revoked'
                }),200
        )
    return res

# response for token refresh request
def tokenRefresh(user, access_token):
    res = make_response(jsonify({ 
                'username': user.username,
                'message': f"Logged in as {user.email}",
                'access_token': access_token,
            }),200
        )
    return res
