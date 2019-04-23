from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, validators

class TrackForm(FlaskForm):
   
    name = SelectField("Track name", [validators.Length(min=3, max=100)], choices=[])
    
    class Meta:
        csrf = False
        