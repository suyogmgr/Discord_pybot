import os
from dotenv import load_dotenv


load_dotenv()

DISCORD_API_SECRET = os.getenv("DICORD_API_TOKEN")