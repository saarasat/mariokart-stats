from application import db

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
  
    handle = db.Column(db.String(160), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, handle):
        self.handle = handle