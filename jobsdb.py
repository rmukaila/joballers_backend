from pymongo import MongoClient
import os

mongo_url = os.getenv('mongodburl') #Note this env is on the cloud not your local

# mongo_url = 'mongodb://localhost:27011'

mongoClNT = MongoClient(mongo_url)

JOB_DB = mongoClNT['jobs_advertisements_db']
job_col = JOB_DB['job_ads']
# mydict = { "name": "John", "address": "Highway 37" }
# mock_data = [{'id':1,'title':"Data engineer",'tags':['mid','python','AWS','GCP'],'description':"Must have GCP certification, etc"},
#     {'id':2,'title':"Data scientist",'tags':['mid','python','R'],'description':"Must have GCP certification"},
#     {'id':3,'title':"python developer",'tags':['mid','python','docker'],'description':"Must have GCP certification"},
#     {'id':4,'title':"full-stack developer",'tags':['mid','python','react'],'description':"Must have GCP certification"}
# ]

# job_col.insert(mock_data)

# print(JOB_DB.list_collection_names())

def get_all_data():
    JOB_DB = mongoClNT['jobs_advertisements_db']
    job_col = JOB_DB['job_ads']
    items_ = [x for x in job_col.find({},{ "_id": 0})]
    return {'data':items_}#job_col.find()

# print(get_all_data())
