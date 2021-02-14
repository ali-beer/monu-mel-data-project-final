from flask_restful import Resource
from flask import request
import pandas as pd
import json

class WelcomeAPI(Resource):
    def get(self):
        ret = ({
                "message": "Welcome to the 'Learning & Development In Children - Data Analysis' API.",
                "routes": [
                    {"/api/g44" : "Census 2016, G44 Labour force status by sex of parents by age of dependent children for Couple families (SA2+)"},
                    {"/api/g45" : "Census 2016, G45 Labour force status by sex of parent by age of dependent children for one parent families (SA2+)"},
                    {"/api/AEDC/communication" : "Census 2016, G45 Labour force status by sex of parent by age of dependent children for one parent families (SA2+)"},
                    {"/api/AEDC/social" : "Census 2016, G45 Labour force status by sex of parent by age of dependent children for one parent families (SA2+)"},
                    {"/api/AEDC/health" : "Census 2016, G45 Labour force status by sex of parent by age of dependent children for one parent families (SA2+)"},
                    {"/api/AEDC/emotional" : "Census 2016, G45 Labour force status by sex of parent by age of dependent children for one parent families (SA2+)"},
                    {"/api/AEDC/language" : "Census 2016, G45 Labour force status by sex of parent by age of dependent children for one parent families (SA2+)"},
                    {"/api/AEDC/oneormore" : "Census 2016, G45 Labour force status by sex of parent by age of dependent children for one parent families (SA2+)"},
                    {"/api/AEDC/twoormore" : "Census 2016, G45 Labour force status by sex of parent by age of dependent children for one parent families (SA2+)"}
                    ]}, 200)
        return ret[0], ret[1]


g44_df = json.loads(pd.read_csv('data/g44.csv', delimiter=',', header=0, index_col=False).to_json(orient="records"))
g45_df = json.loads(pd.read_csv('data/g45.csv', delimiter=',', header=0, index_col=False).to_json(orient="records"))

AEDC_social_df = json.loads(pd.read_csv('data/AEDC/social.csv', delimiter=',', header=0, index_col=False).to_json(orient="records"))
AEDC_communication_df = json.loads(pd.read_csv('data/AEDC/communication.csv', delimiter=',', header=0, index_col=False).to_json(orient="records"))
AEDC_health_df = json.loads(pd.read_csv('data/AEDC/health.csv', delimiter=',', header=0, index_col=False).to_json(orient="records"))
AEDC_emotional_df = json.loads(pd.read_csv('data/AEDC/emotional.csv', delimiter=',', header=0, index_col=False).to_json(orient="records"))
AEDC_language_df = json.loads(pd.read_csv('data/AEDC/language.csv', delimiter=',', header=0, index_col=False).to_json(orient="records"))
AEDC_oneormore_df = json.loads(pd.read_csv('data/AEDC/oneormore.csv', delimiter=',', header=0, index_col=False).to_json(orient="records"))
AEDC_twoormore_df = json.loads(pd.read_csv('data/AEDC/twoormore.csv', delimiter=',', header=0, index_col=False).to_json(orient="records"))

class ABS_G44_API(Resource):

    def get(self):
        ret = (g44_df, 200)
        return ret[0], ret[1]

class ABS_G45_API(Resource):

    def get(self):
        ret = (g45_df, 200)
        return ret[0], ret[1]

class AEDC_SOCIAL_API(Resource):

    def get(self):
        ret = (AEDC_social_df, 200)
        return ret[0], ret[1]


class AEDC_COMMUNICATION_API(Resource):

    def get(self):
        ret = (AEDC_communication_df, 200)
        return ret[0], ret[1]

class AEDC_HEALTH_API(Resource):

    def get(self):
        ret = (AEDC_health_df, 200)
        return ret[0], ret[1]

class AEDC_EMOTIONAL_API(Resource):

    def get(self):
        ret = (AEDC_emotional_df, 200)
        return ret[0], ret[1]


class AEDC_LANGUAGE_API(Resource):

    def get(self):
        ret = (AEDC_language_df, 200)
        return ret[0], ret[1]


class AEDC_ONEORMORE_API(Resource):

    def get(self):
        ret = (AEDC_oneormore_df, 200)
        return ret[0], ret[1]

class AEDC_TWOORMORE_API(Resource):

    def get(self):
        ret = (AEDC_twoormore_df, 200)
        return ret[0], ret[1]