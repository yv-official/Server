from server import db
from datetime import datetime
from passlib.hash import pbkdf2_sha256 as sha256

class About(db.EmbeddedDocument):
    bio: db.StringField()
    birthday: db.StringField()
    hostel: db.StringField()
    homeTown: db.StringField()
    school: db.StringField()
    socialHandles: db.DictField()

class User(db.Document):
    firstName = db.StringField()
    lastName = db.StringField()
    username = db.StringField(unique=True)
    email = db.EmailField(unique=True)
    password = db.StringField()
    phone = db.StringField(max_length = 12)
    gender = db.StringField(max_length = 10)
    branch = db.StringField(max_length=10)
    year = db.StringField(max_length=10)

    about = db.EmbeddedDocumentField(About)
    # connections = db.ListField(db.ReferenceField(User))


    image_file = db.ImageField()
    cover_img = db.StringField()
    createdAt = db.DateTimeField( default=datetime.utcnow ) # utc to keep it universal
    updatedAt = db.DateTimeField( default=datetime.utcnow )


    def __repr__(self):
        return f"User('{self.username}','{self.email}')"



# helper for UserModal

# generate hash
def generate_hash(password):
    return sha256.hash(password)

# verify hash
def verify_hash(password, hash):
    return sha256.verify(password, hash) 