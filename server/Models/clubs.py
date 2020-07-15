from server import db
from datetime import datetime
from Models.users import User

class Clubs(db.document):
    clubAddress: db.StringField(unique=True)
    name: db.StringField()
    description: db.StringField()
    image_file = db.ImageField()
    coverImage = db.StringField()

    members: db.ListField(db.ReferenceField(User))
    admins: db.ListField(db.ReferenceField(User))
    createdAt = db.DateTimeField( default=datetime.utcnow ) # utc to keep it universal
    updatedAt = db.DateTimeField( default=datetime.utcnow )