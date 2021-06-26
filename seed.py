'''Seed file to make samaple data for Users Database'''

from models import User, Post, Tag, PostTag, db
from app import app

#Create all tables
db.drop_all()
db.create_all()

#If table isn't empty, empty it
Pet.query.delete()

