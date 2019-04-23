from application import db
from application.models import Base


class Character(Base):
  
    name = db.Column(db.String(100), nullable=False)
     
    def __init__(self, name):
        self.name = name

