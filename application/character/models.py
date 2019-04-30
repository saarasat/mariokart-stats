from application import db
from application.models import Base
from sqlalchemy.sql import text
from sqlalchemy.orm import relationship, backref

class Character(Base):
  
    name = db.Column(db.String(100), nullable=False)
        
    def __init__(self, name):
        self.name = name

