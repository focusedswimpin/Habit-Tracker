from flask import Flask
from routes import pages
import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def create_app():
    app = Flask(__name__)

    # Get the MongoDB URI and Database name from environment variables
    mongo_uri = os.getenv('MONGO_URI')
    database_name = os.getenv('MONGO_DB_NAME')

    # Create a MongoClient and specify the database name
    client = MongoClient(mongo_uri)
    app.db = client[database_name]

    # Register the blueprint
    app.register_blueprint(pages)

    return app
