from dotenv import load_dotenv
import os

load_dotenv()

discord_token = os.getenv('Discord_Token')

print(discord_token)