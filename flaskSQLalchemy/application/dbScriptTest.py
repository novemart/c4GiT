from application import db

from application.models.heroes import Heroes
from application.models.teams import Teams

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:@localhost/superheroes', echo=True)
Session = sessionmaker(bind=engine)

session = Session()

# team = Teams(affiliation='X-men', objective='Being eXXXtra cool')
# session.add(team)
# session.commit()

# hero = Heroes(name='Clinton Barton', alias='Hawkeye', superPower='Master Archer', teamID=4)
# session.add(hero)
# session.commit()


hero = session.query(Heroes).filter_by(id=2).first()
print(hero.name, hero.superPower, hero.alias, hero.teamID)

hero = session.query(Heroes).filter_by(alias='Iron Man').first()
print(hero.name, hero.superPower, hero.alias, hero.teamID)

team = session.query(Teams).filter_by(id=4).first()
print(team.affiliation, team.objective)
for hero in team.heroes:
    print(hero.name, '=', hero.alias)
