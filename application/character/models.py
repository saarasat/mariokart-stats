from application import db
from application.models import Base
from sqlalchemy.sql import text
from sqlalchemy.orm import relationship, backref

class Character(Base):
  
    name = db.Column(db.String(100), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    
    def __init__(self, name, account_id):
        self.name = name
        self.account_id = account_id

