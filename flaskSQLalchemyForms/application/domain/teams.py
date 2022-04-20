from application import db

# ORM - Object relational mapping - mapping class to a table
# DTO - data transfer object
class Teams(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    affiliation = db.Column(db.String(20), nullable=False)
    objective = db.Column(db.String(30), nullable=False)
    heroes = db.relationship('Heroes', backref='heroes')