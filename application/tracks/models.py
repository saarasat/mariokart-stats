from application import db
from application.models import Base
from sqlalchemy.sql import text
from ..players.models import favoritetracks, Player

class Track(Base):
      
    name = db.Column(db.String(100), nullable=False)
   
    favoritetracks = db.relationship('Player', secondary=favoritetracks, backref=db.backref('tracks', lazy='dynamic'))

    def __init__(self, name):
        self.name = name
        
    @staticmethod
    def tracks_basic_stats(id):
        stmt = text("SELECT DISTINCT(Player.handle), Track.name AS Track,"
        " COUNT(Race.track_id) AS Races,"
        " MIN(Race.finish_time) AS BestTime FROM Track" 
        " LEFT JOIN Race ON Track.id = Race.track_id "
        " LEFT JOIN Player ON Race.player_id = Player.id"
        " WHERE Race.account_id = :id"
        " GROUP BY Track.name ORDER BY Races"
        " DESC").params(id=id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"Player":row[0], "Track":row[1], "Races":row[2], "BestTime":row[3]})

        return response