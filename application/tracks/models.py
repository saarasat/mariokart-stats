from application import db
from application.models import Base
from sqlalchemy.sql import text
from ..players.models import favoriteTracks, Player

class Track(Base):
      
    name = db.Column(db.String(160), nullable=False)
   
    favoriteTracks = db.relationship('Player', secondary=favoriteTracks, backref=db.backref('tracks', lazy='dynamic'))

    def __init__(self, name):
        self.name = name
        
    @staticmethod
    def how_many_times_tracks_played():
        stmt = text("SELECT Track.name AS Track,"
        " COUNT(Race.track_id) AS Races,"
        " MIN(Race.finish_time) AS BestTime,"
        " Player.handle AS Player FROM Track" 
        " LEFT JOIN Race ON Track.id = Race.track_id "
        " LEFT JOIN Player ON Race.player_id = Player.id"
        " WHERE Player IS NOT NULL"
        " GROUP BY Track.name ORDER BY Races, Player.handle")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"Track":row[0], "Races":row[1], "BestTime":row[2], "Player":row[3]})
        print('response', response)

        return response