from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField, IntegerField
class HeroForm(FlaskForm):
    name = StringField('Hero Name')
    alias = StringField('Hero Alias')
    superPower = StringField('Super Power')
    teamID = IntegerField('Team ID')
    submit = SubmitField('Add Hero')
