from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, validators

class TrackForm(FlaskForm):
    cup = StringField("Cup", choices=[])
    name = SelectField("Track name", choices=[])
    
    class Meta:
        csrf = False
        