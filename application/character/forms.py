from flask_wtf import FlaskForm
from wtforms import StringField, validators

class CharacterForm(FlaskForm):
   
    name = StringField("Character name", [validators.Length(min=3, max=100)])
    
    class Meta:
        csrf = False