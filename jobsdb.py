from pymongo import MongoClient
import os
# from .models.db_models import Job
# from .job_exceptions import *

#For production environment
from models.db_models import Job
from job_exceptions import *

from typing import Union


mongo_url = os.getenv('mongodburl') #Note this env is on the cloud not your local
# mongo_url = 'mongodb://localhost:27011'

mongoClNT = MongoClient(mongo_url)

JOB_DB = mongoClNT['jobs_advertisements_db']
job_col = JOB_DB['job_ads']

class Controller_():
    def __init__(self) -> None:
        self.JOB_DB = mongoClNT['jobs_advertisements_db']
        self.job_col = self.JOB_DB['job_ads']
        # self.user_col=

    def get_all_data(self) -> dict:        
        items_ = [x for x in self.job_col.find({},{ "_id": 0})]
        return {'data':items_}#job_col.find()
    
    def post_job(self, job:Job) -> Union[dict,bool]:
        try:
            inserted_job = self.job_col.insert_one(job.dict())
            return inserted_job.inserted_id
        except:
            raise Exception(FAILED_JOB_INSERTION)
            #logging required here
            return False




    # print(get_all_data())
