from application.models.heroes import Heroes
from application.models.teams import Teams
from application import db

def get_all_heroes():
    # alternatively, the db object from application may be used
    # heroes = db.session.query(Heroes)
    # return heroes
    return Heroes.query.all()


def get_hero_by_id(hero_id):
    if hero_id > 0:
        return Heroes.query.get(hero_id)
    else:
        return None


def get_team_by_id(team_id):
    if team_id < 100:
        return Teams.query.get(team_id)
    else:
        return None
