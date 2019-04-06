from application import db
from application.models import Base
from sqlalchemy.sql import text
from sqlalchemy.orm import relationship, backref


favoriteTracks = db.Table('favoriteTracks',
    db.Column('player_id', db.Integer, db.ForeignKey('player.id'), primary_key=True),
    db.Column('track_id', db.Integer, db.ForeignKey('track.id'), primary_key=True)
)

class Player(Base):

    handle = db.Column(db.String(160), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    
    favoriteTracks = db.relationship('Track', secondary=favoriteTracks, backref=db.backref('players', lazy='dynamic', cascade='all,delete-orphan', single_parent=True), cascade="delete")
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=False)

    def __init__(self, handle, character_id):
        self.handle = handle
        self.character_id = character_id

    @staticmethod
    def how_many_races_played(id):
        stmt = text("SELECT Player.handle AS Player,"
        " COUNT(Race.track_id) AS Races FROM Player"
        " JOIN Race ON Player.id = Race.player_id"
        " WHERE Player.id = :id").params(id=id)
        
        res = db.engine.execute(stmt)

        print('res ', res)
        response = []
        for row in res:
            response.append({"Player":row[0], "Races":row[1]})
        print('response', response)

        return response
