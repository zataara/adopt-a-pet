'''Seed file to make samaple data for Users Database'''

from models import User, Post, Tag, PostTag, db
from app import app

#Create all tables
db.drop_all()
db.create_all()

#If table isn't empty, empty it
Pet.query.delete()

#Create some new pets
Fido = Pet(name='Fido', species='Terrier', age=4, photo_url='')
Spot = Pet(name='Spot', species='Beagle', age=1, photo_url='')
Tucker = Pet(name='Tukcker', species='Cockapoo', age=7, photo_url='')
Tywin = Pet(name='Tywin', species='Belgian Shepher', age=6, photo_url='')
Lyra = Pet(name='Lyra', species='Calico', age=1, photo_url='')

#Move new pets to session
db.session.add(Fido)
db.session.add(Spot)
db.session.add(Tucker)
db.session.add(Tywin)
db.session.add(Lyra)

#Commit new pets
db.session.commit()