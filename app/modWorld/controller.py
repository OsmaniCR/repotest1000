import datetime
import json
import requests
from flask import Blueprint, request, Response
from app import app

mod_world = Blueprint('worlds', __name__, url_prefix='/')


@mod_world.route('/worlds', methods=['GET', 'POST'])
def getWorlds():
    # We declare the HOST_API variable from config.py info
    if request.method == 'GET':
        URLWORLDS = app.config.get("HOST_API")
        print(URLWORLDS)
        response = requests.get(URLWORLDS)
        planets = response.json()
        for p in planets.keys():
            if p == 'results':
                planets_list = planets[p]
        solution = []
        for plt in planets_list:
            if plt['climate'] == 'arid':
                residents = []
                for r in plt['residents']:
                    residents.append(requests.get(r).json()['name'])
                solution.append({'planet': plt['name'], 'residents': residents})
        print(solution)
        date = datetime.datetime.now()
        with open('{}{}.json'.format(date.day, date.hour), 'w') as file:
            json.dump(solution, file, indent=4)
        print('Finished')
    return Response(response=json.dumps(solution, default=str), status=200, mimetype='application/json')