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

def spotify_check():
    token = util.prompt_for_user_token(username=username,
                                       scope=scope,
                                       client_id=client_id,
                                       client_secret=client_secret,
                                       redirect_uri=redirect_uri)

    print(token)

    spotify = spotipy.Spotify(auth=token)

    current_playback = spotify.current_playback('DE')
    print(current_playback['device']['id'])
    file_obj = open("output.txt","w+")
    file_obj.write(current_playback)


if __name__ == '__main__':
    spotify_check()