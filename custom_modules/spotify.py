import spotipy
import spotipy.util as util
import os
from dotenv import load_dotenv

load_dotenv()

username = os.environ['SPOTIFY_USERNAME']
client_id = os.environ['SPOTIFY_CLIENT_ID']
client_secret = os.environ['SPOTIFY_CLIENT_SECRET']
redirect_uri = os.environ['SPOTIFY_CALLBACK_URL']
scope = 'user-read-recently-played user-read-playback-state user-modify-playback-state user-read-currently-playing'

def check():
    token = util.prompt_for_user_token(username=username,
                                       scope=scope,
                                       client_id=client_id,
                                       client_secret=client_secret,
                                       redirect_uri=redirect_uri)

    print(token)

    spotify = spotipy.Spotify(auth=token)

    current_playback = spotify.current_playback('DE')
    current_title = current_playback['item']['name']
    current_artist = current_playback['item']['artists'][0]['name']
    print(f"The current song title is: {current_title}")
    print(f"The current artist is: {current_artist}")


if __name__ == '__main__':
    check()