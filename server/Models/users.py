from server import db
from datetime import datetime
from passlib.hash import pbkdf2_sha256 as sha256

class About(db.EmbeddedDocument):
    bio = db.StringField(default="Hey, I'm using HBTU Connect")
    birthday = db.StringField(default=None)
    hostel = db.StringField(default=None)
    homeTown = db.StringField(default=None)
    school = db.StringField(default=None)
    socialHandles = db.DictField(default=None)

class Settings(db.EmbeddedDocument):
    privacy = db.DictField(default={"email": 'private', "phone": 'private', "bio": 'public', "birthday": 'connections', "homeTown": 'public', "school": 'connections', "hostel": 'public', "socialHandles": {}})

class User(db.Document):
    firstName = db.StringField(default=None)
    lastName = db.StringField(default=None)
    username = db.StringField(unique=True)
    email = db.EmailField(unique=True)
    password = db.StringField()
    phone = db.StringField(max_length = 12)
    gender = db.StringField(max_length = 10)
    branch = db.StringField(max_length=10)
    year = db.StringField(max_length=10)
    newUser = db.BooleanField(default=True)

    about = db.EmbeddedDocumentField(About, default=About)
    settings = db.EmbeddedDocumentField(Settings, default=Settings)
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