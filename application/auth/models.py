from application import db
from application.models import Base
from sqlalchemy.orm import relationship, backref


class User(Base):

    __tablename__= "account"

    name = db.Column(db.String(150), nullable=False)
    username = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(150), nullable=False)

    players = db.relationship("Player", backref='account', lazy=True)
    races = db.relationship("Race", backref='account', lazy=True)

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True
    
    def roles(self):
        return ["ADMIN"]