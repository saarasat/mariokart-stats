from flask_wtf import FlaskForm
from wtforms import StringField, validators

class PlayerForm(FlaskForm):
    handle = StringField("Player handle", [validators.Length(min=2)])

    class Meta:
        csrf = False
        