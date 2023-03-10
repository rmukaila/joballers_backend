import pytest
from pymongo import MongoClient
import os
# from .jobsdb import Controller_  #For developement
from jobsdb import Controller_   #for production environment

#Create the controller instance for accessing the database
Controller = Controller_()


# @pytest.fixture
# def job_db():
#     mongo_url = os.getenv('mongodburl')
#     mongoClNT = MongoClient(mongo_url)
#     return mongoClNT['jobs_advertisements_db']

# @pytest.fixture
# def job_col(job_db):
#     return job_db['job_ads']


#Test if import statements meets the render hosting site criteria
#This is because for some reason the import statements that work on developemnt laptop 
#doesnt work in the production environment. Thus before pushing commits these must 
#be checked in the following test case

def test_import_statements():
    pass


def test_fetching_all_jobs():
    data = Controller.get_all_data()
    assert len(data['data'])>5

def test_exception_is_being_raised():
    pass

# def test_post_job()

#def test_add_user()
