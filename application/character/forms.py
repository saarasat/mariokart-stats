from flask_wtf import FlaskForm
from wtforms import StringField

class CharacterForm(FlaskForm):
   
    name = StringField("Character name")
    
    class Meta:
        csrf = False