from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, validators

class TrackForm(FlaskForm):
   
    name = StringField("Track name", [validators.Length(min=3, max=100)])
    
    class Meta:
        csrf = False
        