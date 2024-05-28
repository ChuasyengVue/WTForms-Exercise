from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,TextAreaField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, NumberRange


class AddPetForm(FlaskForm):
    """Form for adding pets"""

    name = StringField("Pet Name",validators=[InputRequired()])
    species = SelectField("Pet Species",choices=[('cat','Cat'),
                                                 ("dog","Dog"),
                                                 ("porcupine","Porcupine")])
    photo_url = StringField("Photo Url",validators=[URL(), Optional()])
    age = IntegerField("Pet Age",validators=[Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField("Notes",validators=[Optional()])


class EditPetForm(FlaskForm):
    """For for editing pets"""

    photo_url = StringField("Photo Url",validators=[URL(), Optional()])
    notes = TextAreaField("Notes",validators=[Optional()])
    available = BooleanField("Available?")