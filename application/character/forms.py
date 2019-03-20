from flask_wtf import FlaskForm
from wtforms import StringField, validators

class CharacterForm(FlaskForm):
    name = StringField("Player handle", [validators.Length(min=2)])
    

    class Meta:
        csrf = False