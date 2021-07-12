from flask_wtf import FlaskForm
from wtforms import StringField, Floatfield
from wtfoms.validators import InputRequired, Optional


class AddPetForm(FlaskForm):
    '''Form for adding new pets to adoption agency page'''

    name = StringField('Pet Name', validators=[InputRequired()])
    species = SelectField('Species', choises=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')])
    photo_url = StringField('Photo Link', validators=[Optional()])
    age = IntegerField('Age', validators=[Optional()])
    notes = StringField('Notes', validators=[Optional()])
    