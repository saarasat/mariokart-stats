from application import db
from application.models import Base
from sqlalchemy.sql import text
from sqlalchemy.orm import relationship, backref
from application.races.models import Race

favoritetracks = db.Table('favoritetracks',
    db.Column('player_id', db.Integer, db.ForeignKey('player.id'), primary_key=True),
    db.Column('track_id', db.Integer, db.ForeignKey('track.id'), primary_key=True),
    db.PrimaryKeyConstraint('player_id', 'track_id')
)

class Player(Base):

    handle = db.Column(db.String(100), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    
    favoritetracks = db.relationship('Track', secondary=favoritetracks, backref=db.backref('players'))
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=False)

    def __init__(self, handle, character_id):
        self.handle = handle
        self.character_id = character_id

    @staticmethod
    def player_basic_stats(id):
        stmt = text("SELECT Player.handle AS Player, Character.name AS Character,"
        " COUNT(Race.track_id) AS Races FROM Player"
        " JOIN Character ON Player.character_id = Character.id"
        " JOIN Race ON Player.id = Race.player_id"
        " WHERE Player.id = :id"
        " GROUP BY Player.handle, Character").params(id=id)
        
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"Player":row[0], "Character":row[1], "Races":row[2]})

        return response

    @staticmethod
    def player_races_won(id):
        stmt = text("SELECT SUM(Race.placement) AS Wins FROM Player"
        " JOIN Race ON Player.id = Race.player_id"
        " WHERE Race.placement = 1 AND Player.id = :id").params(id=id)
        
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"Wins":row[0]})
        
        return response

    @staticmethod
    def player_characters_played(id):
        stmt = text("SELECT Character.name AS Character, COUNT(Race.character_id) AS Races FROM Race"
        " JOIN Character ON Race.character_id = Character.id"
        " WHERE player_id = :id"
        " GROUP BY Character"
        " ORDER BY Character").params(id=id)
        
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"Character":row[0], "Races":row[1]})
        return response

    @staticmethod
    def player_characters_won(id):
        stmt = text("SELECT Character.name AS Character, COUNT(Race.character_id) AS Races FROM Race"
        " JOIN Character ON Race.character_id = Character.id"
        " WHERE player_id = :id AND Race.placement = 1"
        " GROUP BY Character"
        " ORDER BY Character").params(id=id)     
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"Character":row[0], "Wins":row[1]})
        return response

    @staticmethod
    def player_find_favoriteTracks(id):
        stmt = text("SELECT Track.name FROM Track"
        " LEFT JOIN favoritetracks ON Track.id = favoritetracks.track_id"
        " WHERE favoritetracks.player_id = :id").params(id=id)

        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"Track":row[0]})

        return response

    @staticmethod
    def player_tracks_played(id):
        stmt = text("SELECT Track.name AS Track, COUNT(Race.track_id) AS Races FROM Race"
        " JOIN Track ON Race.track_id = Track.id"
        " WHERE player_id = :id"
        " GROUP BY Track"
        " ORDER BY Track.name DESC").params(id=id)
        
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"Track":row[0], "Races":row[1]})

        return response

    @staticmethod
    def player_tracks_won(id):
        stmt = text("SELECT Track.name AS Track, COUNT(Race.track_id) AS Races FROM Race"
        " JOIN Track ON Race.track_id = Track.id"
        " WHERE player_id = :id AND Race.placement = 1"
        " GROUP BY Track"
        " ORDER BY Track.name DESC").params(id=id)
        
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"Track":row[0], "Races":row[1]})

        return response

    @staticmethod
    def player_all_race_stats(id):
        stmt = text("SELECT Track.name AS Track,"
        " Race.finish_time AS FinishTime, Character.name AS Character, Race.placement AS Placement FROM Race"
        " JOIN Track ON Race.track_id = Track.id"
        " JOIN Character ON Race.character_id = Character.id"
        " WHERE player_id = :id"
        " GROUP BY Track, Race.finish_time, Race.placement, Character.name"
        " ORDER BY Race.placement, Race.finish_time").params(id=id)
        
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"Track":row[0],"FinishTime":row[1], "Character":row[2], "Placement":row[3]})

        return response

    @staticmethod
    def player_ranking(id):
        stmt = text("SELECT Player.handle, COUNT(Race.placement) AS Wins FROM Race"
        " JOIN Player ON Player.id = Race.player_id"
        " WHERE Race.placement = 1 AND Player.account_id = :id"
        " GROUP BY Player.handle"
        " ORDER BY Wins DESC").params(id=id)

        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append({"Player":row[0], "Wins":row[1]})

        return response
