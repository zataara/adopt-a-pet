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
Tucker = Pet(name='Tucker', species='Cockapoo', age=7, photo_url='https://instagram.fhio2-2.fna.fbcdn.net/v/t51.2885-15/sh0.08/e35/p640x640/50932757_146767479660275_2932798768252128428_n.jpg?_nc_ht=instagram.fhio2-2.fna.fbcdn.net&_nc_cat=111&_nc_ohc=K4_jBR7sTFcAX9kRUu9&edm=AABBvjUBAAAA&ccb=7-4&oh=e3db3b234232224629f3fbdf67885d98&oe=60FA2ECF&_nc_sid=83d603')
Tywin = Pet(name='Tywin', species='Belgian Shepher', age=6, photo_url='https://instagram.fhio2-2.fna.fbcdn.net/v/t51.2885-15/e35/c0.135.1080.1080a/s240x240/24126402_1962382997415815_4490916034894626816_n.jpg?_nc_ht=instagram.fhio2-2.fna.fbcdn.net&_nc_cat=111&_nc_ohc=s_J_A5WhoEQAX_-vGe6&edm=APU89FABAAAA&ccb=7-4&oh=879bd460163911c30af5f1cf8e7bb2fe&oe=60F9C09C&_nc_sid=86f79a')
Lyra = Pet(name='Lyra', species='Calico', age=1, photo_url='https://instagram.fhio2-2.fna.fbcdn.net/v/t51.2885-15/sh0.08/e35/p640x640/138690753_112096130794180_6133419399508574741_n.jpg?_nc_ht=instagram.fhio2-2.fna.fbcdn.net&_nc_cat=104&_nc_ohc=cqR6oiC8lV8AX_Oy0aD&edm=AP_V10EBAAAA&ccb=7-4&oh=df7cd032f541c624702877deaf70b66e&oe=60F90DC8&_nc_sid=4f375e')

#Move new pets to session
db.session.add(Fido)
db.session.add(Spot)
db.session.add(Tucker)
db.session.add(Tywin)
db.session.add(Lyra)

#Commit new pets
db.session.commit()

