from flask_wtf import FlaskForm
from wtforms import SelectField, StringField

class PlayerForm(FlaskForm):
    handle = StringField("Player handle")
    firstTrack = SelectField("firstTrack", choices=[])
    secondTrack = SelectField("secondTrack", choices=[])
    character = SelectField("Character", choices=[])

    class Meta:
        csrf = False

class SearchForm(FlaskForm):
    handle = SelectField("Player handle", choices=[])

    class Meta:
        csrf = False