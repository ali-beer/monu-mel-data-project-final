from flask_restful import Resource
from flask import request
import pandas as pd
import json

class WelcomeAPI(Resource):
    def get(self):
        ret = ({"message": "Welcome to the 'Learning & Development In Children - Data Analysis' API.", "routes": [{"/api/g44" : "Census 2016, G44 Labour force status by sex of parents by age of dependent children for Couple families (SA2+)"}, {"/api/g45" : "Census 2016, G45 Labour force status by sex of parent by age of dependent children for one parent families (SA2+)"}],}, 200)
        return ret[0], ret[1]

