from flask_restful import reqparse
import server.Models.users as users
import server.Models.jwtblacklist as jwtblacklist
import server.exceptions as exceptions

# Argument Parsers
def register_parser():
    registerparser = reqparse.RequestParser()
    registerparser.add_argument('username', help = 'This Field Cannot be blank', required=True)
    registerparser.add_argument('email', help = 'This Field Cannot be blank', required=True)
    registerparser.add_argument('password', help = 'This Field Cannot be blank', required=True)
    registerparser.add_argument('firstName', help = 'This Field Cannot be blank', required=True)
    registerparser.add_argument('lastName')
    registerparser.add_argument('gender', help = 'This Field Cannot be blank', required=True)
    registerparser.add_argument('phone')
    registerparser.add_argument('branch', help = 'This Field Cannot be blank', required=True)
    registerparser.add_argument('year', help = 'This Field Cannot be blank', required=True)
    return registerparser

def login_parser():
    loginparser = reqparse.RequestParser()
    loginparser.add_argument('username', help='This Field Cannot be blank', required=True)
    loginparser.add_argument('password', help='This Field Cannot be blank', required=True)
    return loginparser

# helper for userRegistration
def userRegister(username, email, password, firstName, lastName, gender, phone, branch, year):
    check_username = users.User.objects(username=username).first()
    check_email = users.User.objects(email=email).first()
    
    if check_username:
        raise exceptions.UsernameAlreadyExist
    elif check_email:
        raise exceptions.EmailAlreadyExist
    else:
        user = users.User(
            username=username, 
            email=email, 
            password=password,
            firstName=firstName,
            lastName=lastName,
            gender=gender,
            phone=phone,
            branch=branch,
            year=year
        )
        return user

def userLogin(username, password):
    user = users.User.objects(username=username).first()
    
    if user:
        if users.verify_hash(password, user.password):
            return user
        else:
            raise exceptions.AuthenticationFailed
    else:
        raise exceptions.UserDoesNotExist

# helper for access token revoke request
def userLogoutAccessToken(jti):
    try:
        jwtblacklist.add_jti_blacklist(jti)
    except:
        raise exceptions.SomethingWentWrong

# helper for refresh token revoke request
def userLogoutRefreshToken(jti):
    try:
        jwtblacklist.add_jti_blacklist(jti)
    except:
        raise exceptions.SomethingWentWrong

# helper for token refresh request
def tokenRefresh(email):
    user = users.User.objects(email=email).first()
    if user:
        return user
    else:
        raise exceptions.AuthenticationFailed
    

