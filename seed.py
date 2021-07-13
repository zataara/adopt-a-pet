'''Seed file to make samaple data for Users Database'''

from models import Pet, db
from app import app

#Create all tables
db.drop_all()
db.create_all()

#If table isn't empty, empty it
Pet.query.delete()

#Create some new pets
Fido = Pet(name='Fido', species='Terrier', age=4, photo_url='https://www.thesprucepets.com/thmb/MFsTgJGoYjjhpLz66NO8Fp-8JxE=/960x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/Westie-74f76b3f57e643639d67298018374e39.jpg')
Spot = Pet(name='Spot', species='Beagle', age=1, photo_url='https://www.dogzone.com/images/breeds/beagle.jpg')
Tucker = Pet(name='Tucker', species='Cockapoo', age=7, photo_url='https://www.instagram.com/p/Bt1t1FAnEPY/?utm_source=ig_embed&amp;utm_campaign=loading')
Tywin = Pet(name='Tywin', species='Belgian Shepher', age=6, photo_url='https://www.instagram.com/p/BcGQEpNF35M/')
Lyra = Pet(name='Lyra', species='Calico', age=1, photo_url='https://www.instagram.com/p/CG3YDdLFNPNTcOCOaqQ5xsfXzGmqcxcLl8OYjU0/')

#Move new pets to session
db.session.add(Fido)
db.session.add(Spot)
db.session.add(Tucker)
db.session.add(Tywin)
db.session.add(Lyra)

#Commit new pets
db.session.commit()