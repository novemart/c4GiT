import json

from flask import render_template, request, jsonify

import service
from application import app


@app.route('/heroes', methods=['GET'])
def show_heroes():
    error = ""
    heroes = service.get_all_heroes()
    if len(heroes) == 0:
        error = "There are no heroes to display"
    return render_template('hero.html', heroes=heroes, message=error)


@app.route('/hero/<int:hero_id>', methods=['GET'])
def show_hero(hero_id):
    error = ""
    hero = service.get_hero_by_id(hero_id)
    print(hero.name, hero.alias)
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


