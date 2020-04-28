import flask
from flask import Flask, request, jsonify
from selenium import webdriver
import time
import os

import scrapeSearch
import restaurants

app = Flask(__name__)
#driver = webdriver.Chrome(executable_path='/Users/dantelacu/Documents/scrape-covid/python-google-places/chromedriver')
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
print("WAITING")
time.sleep(15)
print("waiting end")

@app.route('/api/names', methods=['GET'])
def dataPull2():
    return jsonify(restaurants.main({'lat':37.956821, 'lng':-122.549118}, 'Novato, California'))

@app.route('/api/statuses', methods=['GET'])
def dataPull():

    if 'placeName' in request.args:
        placeName = str(request.args['placeName'])
        (status_array, delivery_array) = scrapeSearch.main(placeName, driver)
        return jsonify({placeName: {'status': status_array, 'delivery': delivery_array }})
    else:
        return "ERROR NAME NOT PROVIDED IN URL"

# if __name__ == '__main__':
#     # sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     # sock.bind(('localhost', 0))
#     # port = sock.getsockname()[1]
#     # sock.close()
#     # app.run(port=port)
