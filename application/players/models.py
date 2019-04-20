from application import db
from application.models import Base
from sqlalchemy.sql import text
from sqlalchemy.orm import relationship, backref
from application.races.models import Race

favoriteTracks = db.Table('favoriteTracks',
    db.Column('player_id', db.Integer, db.ForeignKey('player.id'), primary_key=True),
    db.Column('track_id', db.Integer, db.ForeignKey('track.id'), primary_key=True),
    db.PrimaryKeyConstraint('player_id', 'track_id')
)

class Player(Base):

    handle = db.Column(db.String(160), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    
    favoriteTracks = db.relationship('Track', secondary=favoriteTracks, backref=db.backref('players'))
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=False)

    def __init__(self, handle, character_id):
        self.handle = handle
        self.character_id = character_id

    @staticmethod
    def basic_player_info(id):
        stmt = text("SELECT Player.handle AS Player, Character.name AS Character,"
        " COUNT(Race.track_id) AS Races FROM Player"
        " JOIN Character ON Player.character_id = Character.id"
        " JOIN Race ON Player.id = Race.player_id"
        " WHERE Player.id = :id"
        " GROUP BY Player.handle, Character.name").params(id=id)
        
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"Player":row[0], "Character":row[1], "Races":row[2]})

        return response

    @staticmethod
    def character_with_most_wins(id):
        stmt = text("SELECT Character.name AS Character,"
        " COUNT(Race.id) AS Wins FROM Player"
        " JOIN Race ON Player.id = Race.player_id"
        " JOIN Character ON Race.character_id = Character.id"
        " WHERE Player.id = :id AND Race.placement = 1"
        " GROUP BY Character"
        " ORDER BY Wins DESC").params(id=id)
        
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"Character":row[0], "Wins":row[1]})
        print('response', response)
        return response

    @staticmethod
    def how_many_tracks_played(id):
        stmt = text("SELECT Track.name AS Track, COUNT(Race.track_id) AS Races FROM Race"
        " JOIN Track ON Race.track_id = Track.id"
        " WHERE player_id = :id"
        " GROUP BY Track"
        " ORDER BY Races DESC").params(id=id)
        
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"Track":row[0], "Races":row[1]})

        return response


    @staticmethod
    def race_statistics(id):
        stmt = text("SELECT Track.name AS Track,"
        " Race.finish_time AS FinishTime, Race.placement AS Placement FROM Race"
        " JOIN Track ON Race.track_id = Track.id"
        " WHERE player_id = :id"
        " GROUP BY Track, Race.finish_time, Race.placement"
        " ORDER BY Race.placement, Race.finish_time").params(id=id)
        
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"Track":row[0],"FinishTime":row[1], "Placement":row[2]})

        return response

    @staticmethod
    def delete_player(id):
        stmt = text("DELETE FROM favoriteTracks WHERE player_id = id")
        res = db.engine.execute(stmt)

        response = []
        print('response', response)