#!/usr/bin/python3
"""
flask app
"""

from flask import Flask, Blueprint, jsonify, make_response
from models import storage
from api.v1.views import app_views
from flask_cors import CORS

app = Flask(__name__)

app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown_appcontext(self):
    storage.close()
    
@app.errorhandler(404)
def not_found(error):
    """ returns a JSON-formatted 404 status code response """
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == "__main__" :
    app.run (host='0.0.0.0', port=5000, threaded =True, debug=True)

