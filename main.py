from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
import json

# Load the .env file
load_dotenv()

# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="user-read-recently-played"))

# Fetch and print 1 recent track (as a test)
results = sp.current_user_recently_played(limit=50, after=1751324400000)


df = pd.json_normalize(results["items"])

for col in df.columns:   # this prints all the columns in the df 
    print(col)

df = df[
    ["track.album.artists", 
    "track.album.name", 
    "track.album.release_date", 
    "track.artists", 
    "track.duration_ms", 
    "track.explicit",
    "track.name",
    "track.popularity"]
    ]

print(df)