import pandas as pd
import numpy as np
from collections import defaultdict
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id='a4cd9a0b8ad2434fb6b38dfa7fb2bf27',
                                                           client_secret='4b23b56bbd514c178d0f8341f0b1c61e'))
number_cols = ['valence', 'year', 'acousticness', 'danceability', 'duration_ms', 'energy', 'explicit',
               'instrumentalness', 'key', 'liveness', 'loudness', 'mode', 'popularity', 'speechiness', 'tempo']
def find_song(name: str, year: str) -> pd.core.frame.DataFrame:

    """Find song
    Args:
        name (str): enter name of song for which we gonna search data from Spotify
        year (int): date of song's release

    Returns:
        song_date (pandas.core.frame.DataFrame): return features of song in dataframe format
    """
    song_data = defaultdict()
    results = sp.search(q= 'track: {} year: {}'.format(name,year), limit=1)
    if results['tracks']['items'] == []:
        return None

    results = results['tracks']['items'][0]
    track_id = results['id']
    audio_features = sp.audio_features(track_id)[0]

    song_data['name'] = [name]
    song_data['year'] = [year]
    song_data['explicit'] = [int(results['explicit'])]
    song_data['duration_ms'] = [results['duration_ms']]
    song_data['popularity'] = [results['popularity']]

    for key, value in audio_features.items():
        song_data[key] = value

    return pd.DataFrame(song_data)


def get_song_data(song: dict, spotify_data: pd.core.frame.DataFrame) -> pd.core.frame.DataFrame:
    """Get song data
    Args:
        song (dict): dict of name and year of song
        spotify_data (pandas.core.frame.DataFrame): our dataset of songs

    Returns:
        song_date (pandas.core.frame.DataFrame): return features of song in dataframe format
    """

    try:
        song_data = spotify_data[(spotify_data['name'] == song['name'])
                                 & (spotify_data['year'] == song['year'])].iloc[0]
        return song_data

    except IndexError:
        return find_song(song['name'], song['year'])


def get_mean_vector(song_list: list, spotify_data: pd.core.frame.DataFrame) -> np.ndarray:
    """Get mean vector
    Args:
        song_list (list): dict of name and year of song
        spotify_data (pandas.core.frame.DataFrame): our dataset of songs

    Returns:
        mean_of_song_data (numpy.ndarray): return mean values for each feature of songs in song_list
    """

    song_vectors = []

    for song in song_list:
        song_data = get_song_data(song, spotify_data)
        if song_data is None:
            print('Warning: {} does not exist in Spotify or in database'.format(song['name']))
            continue
        song_vector = song_data[number_cols].values
        song_vectors.append(song_vector.squeeze())
    song_matrix = np.array(list(song_vectors))
    return np.mean(song_matrix, axis=0)


def flatten_dict_list(dict_list: list) -> dict:
    """Flatten dict list
    Args:
        dict_list (list)

    Returns:
        flattened_dict (dict): conver list of dicts in single dict
    """

    flattened_dict = defaultdict()
    for key in dict_list[0].keys():
        flattened_dict[key] = []

    for dictionary in dict_list:
        for key, value in dictionary.items():
            flattened_dict[key].append(value)

    return flattened_dict