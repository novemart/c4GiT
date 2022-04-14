from application import db
from dataclasses import dataclass

# the annotation below will help to trun the Python object into a JSON object
@dataclass
class Heroes(db.Model):
    # the declarations below are important for turning the object into JSON
    id: int
    name: str
    alias: str
    superPower: str

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    alias = db.Column(db.String(50), nullable=False)
    superPower = db.Column(db.String(70), nullable=False)
    teamID = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)