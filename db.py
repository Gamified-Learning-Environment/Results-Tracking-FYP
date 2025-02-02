import pymongo # import pymongo for database connection
from gridfs import GridFS # import GridFS for file storage
from config import MONGODB_URI

# Create database connections
client = pymongo.MongoClient(MONGODB_URI) # create a client
resultsdb = client.get_database('Resultsdatabase') # get the database

results_collection = resultsdb.resultscollection # get the results collection

# Test connection
client.server_info()