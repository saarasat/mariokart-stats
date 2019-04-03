from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, StringField, TimeField, validators

class RaceForm(FlaskForm):
    finish_time = TimeField("Finish time", [validators.InputRequired()])
    placement = SelectField("Placement", choices=[(1,1), (2,2), (3,3), (4,4), (5,5), (6,6), (7,7), (8,8)])
    track = SelectField("Track", choices=[])
    character = SelectField("Character", choices=[])
    player = SelectField("Player", choices=[])

    class Meta:
        csrf = False
        