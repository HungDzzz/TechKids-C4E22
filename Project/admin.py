from mongoengine import Document, StringField

class Admin (Document):
    title = StringField()
    content = StringField()
    code = StringField()