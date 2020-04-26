import flask
from flask import Flask, request, jsonify

import scrapeSearch
import restaurants

app = Flask(__name__)

@app.route('/api/names', methods=['GET'])
def dataPull2():
    return jsonify(restaurants.main({'lat':37.956821, 'lng':-122.549118}, 'Novato, California'))

@app.route('/api/statuses', methods=['GET'])
def dataPull():

    if 'placeName' in request.args:
        placeName = str(request.args['placeName'])
        return jsonify({placeName: {'status': scrapeSearch.main(placeName)}})
    else:
        return "ERROR NAME NOT PROVIDED IN URL"
