from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, validators

class TrackForm(FlaskForm):
    cup = SelectField("Cup", choices=[('Mushroom Cup', 'Mushroom Cup'), ('Flower Cup', 'Flower Cup') ('Star Cup', 'Star Cup'), ('Special Cup', 'Special Cup')])
    name = SelectField("Track name", choices=[])
    
    class Meta:
        csrf = False
        