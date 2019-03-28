from application import db
from application.models import Base

class Track(Base):
      
    name = db.Column(db.String(160), nullable=False)
    cup = db.Column(db.String(160), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, name, cup):
        self.name = name
        self.cup = cup