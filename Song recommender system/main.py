import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Set up the Spotify API client
client_credentials_manager = SpotifyClientCredentials(client_id='986020c2c3fd4d388ed713a54d8e2bfd',
                                                      client_secret='6d1e03137eb0437c9e3a16b6ff58d600')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Define the function to extract audio features for a given track
def get_audio_features(track_id):
    track = sp.track(track_id)
    features = [
        track['artists'][0]['name'],
        track['album']['name'],
        track.get('danceability', 0.5),
        track.get('energy', 0.5),
        track.get('key', 0),
        track.get('loudness', 0),
        track.get('mode', 0),
        track.get('speechiness', 0.5),
        track.get('acousticness', 0.5),
        track.get('instrumentalness', 0.5),
        track.get('liveness', 0.5),
        track.get('valence', 0.5),
        track.get('tempo', 0),
    ]
    return features

def recommend_songs(track_id):
    # Set up the Spotify client
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials())

    # Get track information
    track_info = sp.track(track_id)
    artist_id = track_info['artists'][0]['id']

    # Search for seed artists
    seed_artists = []
    for artist_name in ["Queen", "Led Zeppelin"]:
        result = sp.search(q=artist_name, type='artist', limit=1)
        if result['artists']['items']:
            seed_artists.append(result['artists']['items'][0]['id'])

    # Set up recommendation parameters
    limit = 20
    market = 'IN'
    target_acousticness = 0.5
    target_danceability = 0.5
    target_energy = 0.5
    target_instrumentalness = 0.5
    target_key = 0
    target_liveness = 0.5
    target_loudness = 0
    target_mode = 0
    min_popularity = 50
    max_popularity = 100
    target_speechiness = 0.5
    target_tempo = 0
    target_valence = 0.5

    # Get song recommendations
    recommendations = sp.recommendations(
        limit=limit,
        seed_artists=seed_artists,
        seed_tracks=[track_id],
        market=market,
        target_acousticness=target_acousticness,
        target_danceability=target_danceability,
        target_energy=target_energy,
        target_instrumentalness=target_instrumentalness,
        target_key=target_key,
        target_liveness=target_liveness,
        target_loudness=target_loudness,
        target_mode=target_mode,
        min_popularity=min_popularity,
        max_popularity=max_popularity,
        target_speechiness=target_speechiness,
        target_tempo=target_tempo,
        target_valence=target_valence
    )

    # Print song recommendations
    print("Recommended songs:")
    for track in recommendations['tracks']:
        print(track['name'] + " by " + track['artists'][0]['name'])


# Test the function by recommending songs based on "Bohemian Rhapsody" by Queen
recommend_songs('7tFiyTwD0nx5a1eklYtX2J')
