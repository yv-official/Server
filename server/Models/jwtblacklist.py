from server import jwt,db


class JWTBlacklist(db.Document):
    jti = db.StringField()


# helpers

# add jti to blacklist 
def add_jti_blacklist(jti):
    token = JWTBlacklist(jti=jti)
    token.save()

# check if jti is blacklisted
def is_jti_blacklisted(jti):
    res = JWTBlacklist.objects(jti=jti).first()
    if res:
        return True
    else:
        return False

@jwt.token_in_blacklist_loader
def check_if_token_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return is_jti_blacklisted(jti)    

