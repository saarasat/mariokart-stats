from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, validators

class PlayerForm(FlaskForm):
    handle = StringField("Player handle", [validators.Length(min=3, max=100)])
    firstTrack = SelectField("firstTrack", [validators.InputRequired()], choices=[])
    secondTrack = SelectField("secondTrack", [validators.InputRequired()], choices=[])
    character = SelectField("Character", [validators.InputRequired()], choices=[])

    class Meta:
        csrf = False

class SearchForm(FlaskForm):
    handle = SelectField("Player handle", choices=[])

    class Meta:
        csrf = False