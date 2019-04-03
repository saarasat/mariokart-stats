from application import db
from application.models import Base
from sqlalchemy.sql import text

class Character(Base):
  
    name = db.Column(db.String(160), nullable=False)
        
    def __init__(self, name):
        self.name = name

    @staticmethod
    def find_the_character_with_most_races():
        stmt = text("SELECT Character.name AS Character, COUNT(Race.character_id) FROM Character JOIN Race ON Character.id = Race.character_id GROUP BY Character.name")

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"Character":row[0], "Races":row[1]})
        
        return response