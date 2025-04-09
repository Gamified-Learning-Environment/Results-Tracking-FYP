import pymongo # import pymongo for database connection
from gridfs import GridFS # import GridFS for file storage
import os

# Try to import from config, fall back to environment variable if config not available
try:
    from config import MONGODB_URI
except ImportError:
    # When deployed, get from environment variable
    MONGODB_URI = os.environ.get('MONGODB_URI')
    
    if not MONGODB_URI:
        raise ValueError("MONGODB_URI environment variable not set")


# Create database connections
client = pymongo.MongoClient(MONGODB_URI) # create a client
resultsdb = client.get_database('Resultsdatabase') # get the database

results_collection = resultsdb.resultscollection # get the results collection

# Test connection
client.server_info()