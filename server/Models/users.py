from server import db
from datetime import datetime
from passlib.hash import pbkdf2_sha256 as sha256


class User(db.Document):
    username = db.StringField()
    email = db.EmailField()
    image_file = db.ImageField()
    password = db.StringField()
    createdAt = db.DateTimeField( default=datetime.utcnow ) # utc to keep it universal

    def __repr__(self):
        return f"User('{self.username}','{self.email}')"



# helper for UserModal

# generate hash
def generate_hash(password):
    return sha256.hash(password)

# verify hash
def verify_hash(password, hash):
    return sha256.verify(password, hash) 