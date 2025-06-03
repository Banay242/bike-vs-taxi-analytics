import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
MAPBOX_API_KEY = os.getenv("MAPBOX_API_KEY")

print(">>> superset_config.py LOADED")
