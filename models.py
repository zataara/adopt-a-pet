from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

def connect_db(app):
        db.app = app
        db.init_app(app)

GENERIC_IMAGE = 'http://clipart-library.com/images/di4oLK9jT.jpg'


class Pet(db.Model):
    '''Database model for Users'''

    __tablename__ = 'pets'

    def __repr__(self):
        '''Show additional info about the user'''
        u = self
        return f'<User {u.id} {u.first_name} {u.last_name} {u.img_url}'

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    name = db.Column(db.String(30),
                            nullable=False)
    species = db.Column(db.String(30),
                            nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean,
                            nullable=False,
                            default=True)
    def image_url(self):
        '''return an image for the pet, or a generic if not present'''
        return self.photo_url or GENERIC_IMAGE
                            

