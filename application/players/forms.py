from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, validators

class PlayerForm(FlaskForm):
    handle = StringField("Player handle", [validators.Length(min=2)])
    firstTrack = SelectField("firstTrack", [validators.Length(min=2)], choices=[])
    secondTrack = SelectField("secondTrack", [validators.Length(min=2)], choices=[])
    character = SelectField("Character", [validators.Length(min=2)], choices=[])

    class Meta:
        csrf = False

class SearchForm(FlaskForm):
    handle = SelectField("Player handle", choices=[])

    class Meta:
        csrf = False