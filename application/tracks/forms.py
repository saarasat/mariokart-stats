from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, validators

class TrackForm(FlaskForm):
   
    name = SelectField("Track name", choices=[])
    
    class Meta:
        csrf = False
        