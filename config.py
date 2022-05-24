import os

from dotenv import load_dotenv

load_dotenv()

class MongoDBConfig:
  USERNAME = os.environ.get("MONGO_USERNAME") or ""
  PASSWORD = os.environ.get("MONGO_PASSWORD") or ""
  HOST = os.environ.get("MONGO_HOST") or "localhost"
  PORT = os.environ.get("MONGO_PORT") or "27017"
  DATABASE = os.environ.get("MONGO_DBS") or ""
  LINKS_COLLECTION = os.environ.get("MONGO_LINKS_COLLECTION") or ""
  URLS_COLLECTION = os.environ.get("MONGO_URLS_COLLECTION") or ""