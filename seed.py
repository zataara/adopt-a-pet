'''Seed file to make samaple data for Users Database'''

from models import User, Post, Tag, PostTag, db
from app import app

#Create all tables
db.drop_all()
db.create_all()

#If table isn't empty, empty it
Pet.query.delete()

#Create some new pets
Fido = Pet(name='Fido', species='Terrier', age=4, photo_url='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.thesprucepets.com%2Fterrier-dog-breeds-5112878&psig=AOvVaw2a9GJ9-3GA1j7bOdcloZ8L&ust=1625715349389000&source=images&cd=vfe&ved=0CAoQjRxqFwoTCNjxnuGD0PECFQAAAAAdAAAAABAE')
Spot = Pet(name='Spot', species='Beagle', age=1, photo_url='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.dogzone.com%2Fbreeds%2Fbeagle%2F&psig=AOvVaw2jSg5c_N2F48Z3KNS5DflN&ust=1625715312424000&source=images&cd=vfe&ved=0CAoQjRxqFwoTCOjL0c-D0PECFQAAAAAdAAAAABAJ')
Tucker = Pet(name='Tukcker', species='Cockapoo', age=7, photo_url='https://www.instagram.com/p/Bt1t1FAnEPY/')
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