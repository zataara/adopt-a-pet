from flask_wtf import FlaskForm
from wtforms import StringField, Floatfield


class AddPetForm(FlaskForm):
    '''Form for adding new pets to adoption agency page'''

    name = StringField('Pet Name')
    species = StringField('Species')
    photo_url = StringField('Photo Link')
    age = IntegerField('Age')
    notes = StringField('Notes')