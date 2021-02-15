from flask_restful import Resource
from flask import request
import pandas as pd
import json

class WelcomeAPI(Resource):
    def get(self):
        ret = ({
                "message": "Welcome to the 'Learning & Development In Children - Data Analysis' API.",
                "routes": [
                    {"/api/ABS" : "Our polished ABS dataset"},
                    {"/api/ABS/g44A" : "Census 2016, G44 Labour force status by sex of parents by age of dependent children for Couple families (SA2+)"},
                    {"/api/ABS/g44A_descriptors" : "Descriptors for Census 2016, G44 Labour force status by sex of parents by age of dependent children for Couple families (SA2+)"},
                    {"/api/ABS/g45A" : "Census 2016, G45 Labour force status by sex of parent by age of dependent children for one parent families (SA2+)"},
                    {"/api/ABS/g45B" : "Census 2016, G45 Labour force status by sex of parent by age of dependent children for one parent families (SA2+)"},
                    {"/api/AEDC/communication" : "Census 2016, G45 Labour force status by sex of parent by age of dependent children for one parent families (SA2+)"},
                    {"/api/AEDC/social" : "Census 2016, G45 Labour force status by sex of parent by age of dependent children for one parent families (SA2+)"},
                    {"/api/AEDC/health" : "Census 2016, G45 Labour force status by sex of parent by age of dependent children for one parent families (SA2+)"},
                    {"/api/AEDC/emotional" : "Census 2016, G45 Labour force status by sex of parent by age of dependent children for one parent families (SA2+)"},
                    {"/api/AEDC/language" : "Census 2016, G45 Labour force status by sex of parent by age of dependent children for one parent families (SA2+)"},
                    {"/api/AEDC/oneormore" : "Census 2016, G45 Labour force status by sex of parent by age of dependent children for one parent families (SA2+)"},
                    {"/api/AEDC/twoormore" : "Census 2016, G45 Labour force status by sex of parent by age of dependent children for one parent families (SA2+)"}
                    ]}, 200)
        return ret[0], ret[1]

# ABS
ABS_df = json.loads(pd.read_csv('data/ABS/clean_2016_abs.csv', delimiter=',', header=0, index_col=False).to_json(orient="records"))
g44A_descriptors_df = json.loads(pd.read_csv('data/ABS/2016Census_G44A_cell_descriptors.csv', delimiter=',', header=0, index_col=False).to_json(orient="records"))
g44A_df = json.loads(pd.read_csv('data/ABS/2016Census_G44A_VIC_SA2.csv', delimiter=',', header=0, index_col=False).to_json(orient="records"))
g45A_df = json.loads(pd.read_csv('data/ABS/2016Census_G45A_VIC_SA2.csv', delimiter=',', header=0, index_col=False).to_json(orient="records"))
g45B_df = json.loads(pd.read_csv('data/ABS/2016Census_G45B_VIC_SA2.csv', delimiter=',', header=0, index_col=False).to_json(orient="records"))

#AEDC
AEDC_social_df = json.loads(pd.read_csv('data/AEDC/social.csv', delimiter=',', header=0, index_col=False).to_json(orient="records"))
AEDC_communication_df = json.loads(pd.read_csv('data/AEDC/communication.csv', delimiter=',', header=0, index_col=False).to_json(orient="records"))
AEDC_health_df = json.loads(pd.read_csv('data/AEDC/health.csv', delimiter=',', header=0, index_col=False).to_json(orient="records"))
AEDC_emotional_df = json.loads(pd.read_csv('data/AEDC/emotional.csv', delimiter=',', header=0, index_col=False).to_json(orient="records"))
AEDC_language_df = json.loads(pd.read_csv('data/AEDC/language.csv', delimiter=',', header=0, index_col=False).to_json(orient="records"))
AEDC_oneormore_df = json.loads(pd.read_csv('data/AEDC/oneormore.csv', delimiter=',', header=0, index_col=False).to_json(orient="records"))
AEDC_twoormore_df = json.loads(pd.read_csv('data/AEDC/twoormore.csv', delimiter=',', header=0, index_col=False).to_json(orient="records"))

class ABS_API(Resource):

    def get(self):
        ret = (ABS_df, 200)
        return ret[0], ret[1]

class ABS_G44A_API(Resource):

    def get(self):
        ret = (g44A_df, 200)
        return ret[0], ret[1]

class ABS_G44A_DESCRIPTORS_API(Resource):

    def get(self):
        ret = (g44A_descriptors_df, 200)
        return ret[0], ret[1]

class ABS_G45A_API(Resource):

    def get(self):
        ret = (g45A_df, 200)
        return ret[0], ret[1]

class ABS_G45B_API(Resource):

    def get(self):
        ret = (g45B_df, 200)
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