from application import db

class Race(db.Model):
    id = db.Column(db.Integer, primary_key=True)
  
    finish_time = db.Column(db.Time, nullable=True)
    placement = db.Column(db.Integer, nullable=False)

    character_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=False)
    track_id = db.Column(db.Integer, db.ForeignKey('track.id'), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, placement, finish_time, track_id, character_id):
        self.placement = placement
        self.finish_time = finish_time
        self.track_id = track_id
        self.character_id = character_id