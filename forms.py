from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, Length, NumberRange


class AddPetForm(FlaskForm):
    '''Form for adding new pets to adoption agency page'''

    name = StringField('Pet Name', validators=[InputRequired()])
    species = SelectField('Species', choises=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')])
    photo_url = StringField('Photo URL', validators=[Optional(), URL()])
    age = IntegerField('Age', validators=[Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField('Comments', validators=[Optional(), Length(min=10)])



class EditPetForm(FlaskForm):
    '''Form for editing an existsing pet at the adoption agency'''

    photo_url = StringField('Photo URL', validators=[Optional(), URL()])
    notes = StringField('Notes', validators=[Optional(), Length(min=10)])
    available = BooleanField('Available?')
    