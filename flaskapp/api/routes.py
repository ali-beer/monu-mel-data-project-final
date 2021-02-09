from flask import Blueprint, jsonify, request
from flaskapp.api.resources import WelcomeAPI
from flask_cors import cross_origin

# Initiating API blueprint
api_bp = Blueprint('api', __name__)


# Intializing API routes function used when intializing the app
def initialise_api_routes(api):
    api.add_resource(WelcomeAPI, '/api')