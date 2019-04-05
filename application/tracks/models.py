from application import db
from application.models import Base
from sqlalchemy.sql import text
from ..players.models import favoriteTracks

class Track(Base):
      
    name = db.Column(db.String(160), nullable=False)
   
    favoriteTracks = db.relationship('Player', secondary=favoriteTracks, backref=db.backref('tracks', lazy='dynamic'))

    def __init__(self, name):
        self.name = name
        

    @staticmethod
    def how_many_times_tracks_played():
        stmt = text("SELECT Track.name AS Track, COUNT(Race.track_id) AS Races FROM Track LEFT JOIN Race ON Track.id = Race.track_id GROUP BY Track.name ORDER BY Races DESC")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"Track":row[0], "Races":row[1]})
        
        return response