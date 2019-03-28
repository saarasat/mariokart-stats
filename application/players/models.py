from application import db
from application.models import Base
from sqlalchemy.sql import text
from sqlalchemy.orm import relationship, backref
from ..races.models import playersraces


class Player(Base):

    handle = db.Column(db.String(160), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    playersraces = db.relationship('Race', secondary=playersraces, backref=db.backref('players', lazy='dynamic'))

    def __init__(self, handle):
        self.handle = handle

