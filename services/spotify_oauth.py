import spotipy
from spotipy.oauth2 import SpotifyOAuth
SPOTIFY_CLIENT_ID = "ef05fc98d68d46298e93a2da2b717946"
SPOTIFY_CLIENT_SECRET = "15e5ce3c623e41b09b85c37d125d2021"
SPOTIFY_REDIRECT_URI = "https://5000-hulorenzo-refactoringsp-uit22q6hudz.ws-eu117.gitpod.io/callback"

sp_oauth = SpotifyOAuth(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope="user-read-private",
    show_dialog=True
)

def get_spotify_object(token_info):
    return spotipy.Spotify(auth=token_info['access_token'])