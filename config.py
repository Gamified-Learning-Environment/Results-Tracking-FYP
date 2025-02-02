import os
from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = os.environ.get('MONGODB_URI')

if not MONGODB_URI:
    raise ValueError("Missing required environment variables. Please check your .env file")