from flask import render_template, request, jsonify

from application import app, service
from application.forms.heroForm import HeroForm
from application.domain.heroes import Heroes

@app.route('/')
@app.route('/heroes', methods=['GET'])
def show_heroes():
    error = ""
    heroes = service.get_all_heroes()
    if len(heroes) == 0:
        error = "There are no heroes to display"
    return render_template('hero.html', heroes=heroes, message=error)

# for the sake of example
@app.route('/hero/<int:hero_id>', methods=['GET'])
def show_hero(hero_id):
    error = ""
    hero = service.get_hero_by_id(hero_id)
    # for the sake of debugging
    # print(hero.name, hero.alias)
    if not hero:
        return jsonify("There is no heroes with ID: " + str(hero_id))
    return jsonify(hero)


@app.route('/teamandheroes/<int:team_id>', methods=['GET'])
def team_and_heroes(team_id):
    error = ""
    team = service.get_team_by_id(team_id)
    if not team:
        error = "There is no team with ID: " + str(team_id)
    return render_template('teams_and_heroes.html', team=team, message=error, title="Team and its Heroes")

@app.route('/new_hero', methods=['GET','POST'])
def add_new_hero():
    error = ""
    form = HeroForm()

    if request.method == 'POST':
        form = HeroForm(request.form)
        print(form.name.data)
        name = form.name.data
        alias = form.alias.data
        superPower = form.superPower.data
        teamID = form.teamID.data


        if len(name) == 0 or len(alias) == 0:
            error = "Please supply both name and alias"
        else:
            hero = Heroes(name=name, alias=alias, superPower = superPower, teamID = teamID)
            service.add_new_hero(hero)
            heroes = service.get_all_heroes()
            return render_template('hero.html', heroes=heroes, message=error)

    return render_template('new_hero_form.html', form=form, message=error)
