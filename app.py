from flask import Flask, make_response
import json
import time
# from .jobsdb import Controller_  #Note: this way of importing is the one supported by render hosting site. to run the service on local machine, use ".jobsdb " or "flask_backend.jobsdb"

from jobsdb import Controller_  #For prod environment






app = Flask(__name__)

#Create the controller instance for accessing the database
Controller = Controller_()



@app.route('/')
def hello():
    return "<p>This is just a headless webservice to expose a few apis. No template nor static files</p>"

@app.route("/all_job_terms")
def get_all_terms():
    #Fetch data from mongodb and return them as json
    data = Controller.get_all_data()
    respons = make_response(json.dumps(data))
    respons.headers['Access-Control-Allow-Origin'] = '*'
    # time.sleep(2) #for testing situation of slow network

    return respons
