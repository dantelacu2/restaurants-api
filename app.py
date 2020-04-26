import flask
from flask import Flask, request, jsonify

import scrapeSearch

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def dataPull():

    if 'placeName' in request.args:
        placeName = str(request.args['placeName'])
        return jsonify({placeName: {'status': scrapeSearch.main(placeName)}})
    else:
        return "ERROR NAME NOT PROVIDED IN URL"
