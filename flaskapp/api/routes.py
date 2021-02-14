from flask import Blueprint, jsonify, request
from flaskapp.api.resources import *
from flask_cors import cross_origin

# Initiating API blueprint
api_bp = Blueprint('api', __name__)


# Intializing API routes function used when intializing the app
def initialise_api_routes(api):
    api.add_resource(WelcomeAPI, '/api')
    api.add_resource(ABS_G44_API, '/api/g44')
    api.add_resource(ABS_G45_API, '/api/g45')
    api.add_resource(AEDC_SOCIAL_API, '/api/AEDC/social')
    api.add_resource(AEDC_HEALTH_API, '/api/AEDC/health')
    api.add_resource(AEDC_EMOTIONAL_API, '/api/AEDC/emotional')
    api.add_resource(AEDC_LANGUAGE_API, '/api/AEDC/language')
    api.add_resource(AEDC_COMMUNICATION_API, '/api/AEDC/communication')
    api.add_resource(AEDC_ONEORMORE_API, '/api/AEDC/oneormore')
    api.add_resource(AEDC_TWOORMORE_API, '/api/AEDC/twoormore')