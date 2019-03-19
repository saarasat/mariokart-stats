from application import db

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
  
    handle = db.Column(db.String(160), nullable=True)

    def __init__(self, handle):
        self.handle = handle