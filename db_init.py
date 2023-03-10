from pymongo import MongoClient
import os

if __name__=='__main__':
    """
    The following code will be called when starting the app's docker image for the first time
    help initialise the database when using the docker image of the app
    """
    
    mock_data = [{'id':1,'title':"Data engineer",'tags':['mid','python','AWS','GCP'],'description':"Must have GCP certification, etc"},
    {'id':2,'title':"Data scientist",'tags':['mid','python','R'],'description':"Must have GCP certification"},
    {'id':3,'title':"python developer",'tags':['mid','python','docker'],'description':"Must have GCP certification"},
    {'id':4,'title':"full-stack developer",'tags':['mid','python','react'],'description':"Must have GCP certification"}
    ]

    mongo_url = os.getenv('mongodburl')
    mongoClNT = MongoClient(mongo_url)

    JOB_DB = mongoClNT['jobs_advertisements_db']
    job_col = JOB_DB['job_ads']
    job_col.insert(mock_data)

    print(JOB_DB.list_collection_names())