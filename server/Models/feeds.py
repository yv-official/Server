from server import db
from datetime import datetime
from Models.users import User

#embedded document for ask model
class Question(db.EmbeddedDocument):
    body= db.ListField()
    title= db.StringField()
    tags= db.ListField()
    comments= db.ListField()
    upvotes= db.StringField()
    stars= db.ListField()
    views= db.StringField()

#embedded document for ask model
class Answers(db.EmbeddedDocument):
    body= db.ListField()
    comments= db.ListField()
    upvotes= db.StringField()
    stars= db.StringField()

    addedBy= db.RefrenceField(User)
    createdAt = db.DateTimeField( default=datetime.utcnow )
    updatedAt = db.DateTimeField( default=datetime.utcnow )

    

class Ask(db.document):
    createdAt = db.DateTimeField( default=datetime.utcnow )
    updatedAt = db.DateTimeField( default=datetime.utcnow )

    question= db.EmbeddedDocumentField(Question)
    privacy= db.StringField()
    answers= db.ListField(db.EmbeddedDocumentField(Answers))
    askedBy= db.RefrenceField(User)

#ask model ends

#blogs model
class Blog(db.document):
    createdAt = db.DateTimeField( default=datetime.utcnow )
    updatedAt = db.DateTimeField( default=datetime.utcnow )
    writtenBy = db.RefrenceField(User)

    title = db.StringField()
    subTitle = db.StringField()
    body = db.ListField()
    tags = db.ListField()
    stars = db.StringField()
    views = db.StringField()
    
    comments = db.ListField()

