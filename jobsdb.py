from pymongo import MongoClient

mongo_url = 'mongodb://localhost:27011'

mongoClNT = MongoClient(mongo_url)

JOB_DB = mongoClNT['jobs_advertisements_db']
job_col = JOB_DB['job_ads']
# mydict = { "name": "John", "address": "Highway 37" }

# job_col.insert(mydict)

# print(JOB_DB.list_collection_names())

def get_all_data():
    JOB_DB = mongoClNT['jobs_advertisements_db']
    job_col = JOB_DB['job_ads']
    items_ = [x for x in job_col.find({},{ "_id": 0})]
    return {'data':items_}#job_col.find()

# print(get_all_data())