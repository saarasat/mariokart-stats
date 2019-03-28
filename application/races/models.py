from application import db
from application.models import Base
from sqlalchemy.sql import text
from sqlalchemy.orm import relationship, backref


playersraces = db.Table('playersraces',
    db.Column('player_id', db.Integer, db.ForeignKey('player.id'), primary_key=True),
    db.Column('race_id', db.Integer, db.ForeignKey('race.id'), primary_key=True)
)

class Race(Base):
  
    finish_time = db.Column(db.Time, nullable=True)
    placement = db.Column(db.Integer, nullable=False)

    character_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=False)
    track_id = db.Column(db.Integer, db.ForeignKey('track.id'), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    playersraces = db.relationship('Player', secondary=playersraces, backref=db.backref('races', lazy='dynamic'))


    def __init__(self, placement, finish_time, track_id, character_id):
        self.placement = placement
        self.finish_time = finish_time
        self.track_id = track_id
        self.character_id = character_id


    @staticmethod
    def find_placements_in_mushroom_cup():
        stmt = text("SELECT placement, finish_time FROM Race "
        "JOIN Track ON Track.id = Race.track_id"
        "WHERE Track.cup = 'Mushroom Cup'"
        "GROUP BY Track.name"
        "SORT BY Race.placement")

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"placement":row[0], "finish_time":row[1]})
        
        return response