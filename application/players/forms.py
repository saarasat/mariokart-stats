from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, validators

class PlayerForm(FlaskForm):
    handle = StringField("Player handle", [validators.Length(min=2)])
    firstTrack = SelectField("firstTrack", choices=[])
    secondTrack = SelectField("secondTrack", choices=[])
    character = SelectField("Character", choices=[])

    class Meta:
        csrf = False

class SearchForm(FlaskForm):
    handle = SelectField("Player handle", choices=[])

    class Meta:
        csrf = False