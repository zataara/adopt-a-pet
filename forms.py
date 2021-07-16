from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Optional


class AddPetForm(FlaskForm):
    '''Form for adding new pets to adoption agency page'''

    name = StringField('Pet Name', validators=[InputRequired()])
    species = SelectField('Species', choises=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')])
    photo_url = StringField('Photo Link', validators=[Optional()])
    age = IntegerField('Age', validators=[Optional()])
    notes = StringField('Notes', validators=[Optional()])



class EditPetForm(FlaskForm):
    '''Form for editing an existsing pet at the adoption agency'''

    photo_url = StringField('Photo URL', validators=[Ooptional()])
    notes = StringField('Notes', validators=[Optional()])
    available = BooleanField('Is Available?', validators=[InputRequired()])
    