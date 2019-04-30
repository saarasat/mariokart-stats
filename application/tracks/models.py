from application import db
from application.models import Base
from sqlalchemy.sql import text
from ..players.models import favoritetracks, Player

class Track(Base):
      
    name = db.Column(db.String(100), nullable=False)
   
    favoritetracks = db.relationship('Player', secondary=favoritetracks, backref=db.backref('tracks', lazy='dynamic'))
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, name, account_id):
        self.name = name
        self.account_id = account_id
        
    @staticmethod
    def tracks_basic_stats(id):
        stmt = text("SELECT Track.name AS Track,"
        " COUNT(Race.track_id) AS Races,"
        " MIN(Race.finish_time) AS BestTime,"
        " Player.handle AS Player FROM Track" 
        " LEFT JOIN Race ON Track.id = Race.track_id "
        " LEFT JOIN Player ON Race.player_id = Player.id"
        " WHERE Race.account_id = :id"
        " GROUP BY Track.name, Player.handle ORDER BY Races"
        " DESC").params(id=id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"Track":row[0], "Races":row[1], "BestTime":row[2], "Player":row[3]})

        return response