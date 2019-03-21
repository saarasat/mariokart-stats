from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, StringField, TimeField, validators

class RaceForm(FlaskForm):
    finish_time = TimeField("Finish time", [validators.InputRequired()])
    placement = IntegerField("Placement", [validators.InputRequired()])
    track = SelectField("Track", choices=[])
    character = SelectField("Character", choices=[])

    class Meta:
        csrf = False
        