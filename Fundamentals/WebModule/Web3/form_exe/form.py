from mongoengine import Document, StringField, ListField, IntField

class Form (Document):
    firstname = StringField()
    lastname = StringField()
    email = StringField()
    yob = IntField()
    gender = StringField()
    city = StringField()
    #code = StringField()
