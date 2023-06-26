import requests
from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route('/scrape', methods = ['GET', 'POST'])
def handle_request():
    if request.method == 'GET':
        return "Hello, Flask!"
    
    if request.method == 'POST':
        return get_scraped_data(request.get_json()) if request.get_json() else jsonify({})
    
def get_scraped_data(jsonData):
    jsonify(jsonData)
    pass

def scrape():
    pass
    #requests.get("craigslist.com")