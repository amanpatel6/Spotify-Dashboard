import os
from dotenv import load_dotenv
import requests
import pandas as pd
import spotipy

load_dotenv()
client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
spotify_redirect_uri = os.getenv("uri")

url = "https://api.spotify.com/v1/me/player/recently-played?limit=50&after=1750940400000"

request = spotipy.