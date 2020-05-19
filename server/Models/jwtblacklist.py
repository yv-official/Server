from server import jwt,db


class JWTBlacklist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(200), nullable=False)


# helpers

# add jti to blacklist 
def add_jti_blacklist(jti):
    token = JWTBlacklist(jti=jti)
    db.session.add(token)
    db.session.commit()

# check if jti is blacklisted
def is_jti_blacklisted(jti):
    res = JWTBlacklist.query.filter_by(jti=jti).first()
    if res:
        return True
    else:
        return False

@jwt.token_in_blacklist_loader
def check_if_token_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return is_jti_blacklisted(jti)    

