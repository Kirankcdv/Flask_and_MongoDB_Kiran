
import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()
uri = os.getenv("MONGO_URI")

if not uri:
    print("ERROR: MONGO_URI is missing.")
else:
    client = MongoClient(uri, serverSelectionTimeoutMS=5000)
    try:
        client.admin.command("ping")
        print("SUCCESS: MongoDB Atlas connection works!")
    except Exception as error:
        print("ERROR TYPE:", type(error).__name__)
        print("DETAILS:", str(error)[:500])
    finally:
        client.close()
