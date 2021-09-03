from flask import Flask, request, render_template, redirect, flash, session, url_for
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt-a-pet'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


connect_db(app)
db.create_all()

### Main routes
@app.route('/')
def list_pets():
    '''Homepage redirects to list of all users'''
    pets = Pet.query.all()


    return render_template('index.html', pets=pets)

#
@app.route('/add', methods=['GET', 'POST'])
def show_add_form():
    '''Page to add a new pet to the adoption agency'''
    
    form = AddPetForm()
    
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        return redirect(url_for('list_pets'))
    else:
        return render_template('add.html', form=form, pet=pet)


@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def show_pet_detail(pet_id):
    '''Page to show details and edit an existing pet at the adoption page'''
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect(url_for('list_pets'))
    else:
        return render_template('detail.html', form=form, pet=pet)