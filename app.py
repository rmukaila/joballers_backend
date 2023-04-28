from flask import Flask, make_response
import json
import time
from .jobsdb import get_all_data  #Note: this way of importing is the one supported by render hosting site. to run the service on local machine, use ".jobsdb " or "flask_backend.jobsdb"


app = Flask(__name__)

# mock_data = [{'id':1,'title':"Data engineer",'tags':['mid','python','AWS','GCP'],'description':"Must have GCP certification, etc"},
#     {'id':2,'title':"Data scientist",'tags':['mid','python','R'],'description':"Must have GCP certification"},
#     {'id':3,'title':"python developer",'tags':['mid','python','docker'],'description':"Must have GCP certification"},
#     {'id':4,'title':"full-stack developer",'tags':['mid','python','react'],'description':"Must have GCP certification"}
#           ]

@app.route('/')
def hello():
    return "<p>This is just a headless webservice to expose a few apis. No template nor static files</p>"

@app.route("/all_job_terms")
def get_all_terms():
    #Fetch data from mongodb and return them as json
    data = get_all_data()
    respons = make_response(json.dumps(data))
    respons.headers['Access-Control-Allow-Origin'] = '*'
    # time.sleep(2) #for testing situation of slow network

    return respons
