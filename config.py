import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
MONGODB_URI = os.environ.get('MONGODB_URI')

if not MONGODB_URI: # If MONGODB_URI is not set in the environment
    raise ValueError("Missing required environment variables. Please check your .env file")