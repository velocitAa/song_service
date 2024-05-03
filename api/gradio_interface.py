import random

import gradio as gr
from scipy.spatial.distance import cdist
import numpy as np
import pandas as pd
import joblib

# RECOMMENDATION PART

from recommendation import flatten_dict_list, get_mean_vector

song_kmeans_pipeline = joblib.load('C:/Users/te200/coursework_ML/Weights/kmeans_pipline.pkl')
df = pd.read_csv('C:/Users/te200/coursework_ML/data/data_for_gradio_rec.csv')
names = df[['name']].values.flatten()
years = df[['year']].values.flatten()
number_cols = ['valence', 'year', 'acousticness', 'danceability', 'duration_ms', 'energy', 'explicit',
               'instrumentalness', 'key', 'liveness', 'loudness', 'mode', 'popularity', 'speechiness', 'tempo']


def recommend_songs(song_list: str, n_songs) -> dict:
    """Recommend songs
    Args:
        song_list (list): dict of name and year of song
        spotify_data (pandas.core.frame.DataFrame): our dataset of songs
        n_songs (int): number of songs to reccomend

    Returns:
        rec_songs (dict): dict of recommended songs
    """

    metadata_cols = ['name', 'year', 'artists']
    names = []
    years = []
    values = []
    for name in song_list.split(', ')[::2]:
        names.append(name)
    for year in song_list.split(', ')[1::2]:
        years.append(year)

    for idx in range(len(names)):
        tmp = {'name': names[idx], 'year': int(years[idx])}
        values.append(tmp)

    song_dict = flatten_dict_list(values)

    song_center = get_mean_vector(values, df)
    scaler = song_kmeans_pipeline.steps[0][1]
    scaled_data = scaler.transform(df[number_cols])
    scaled_song_center = scaler.transform(song_center.reshape(1, -1))
    distances = cdist(scaled_song_center, scaled_data, 'cosine')
    index = list(np.argsort(distances)[:, :n_songs][0])

    rec_songs = df.iloc[index]
    rec_songs = rec_songs[~rec_songs['name'].isin(song_dict['name'])]

    return pd.DataFrame(rec_songs[metadata_cols].to_dict(orient='records'))[['name', 'artists']]


# CLASSIFICATION PART

import librosa
from models import Model_Genre_Classification, Model_Mood_Classification

genres = {'blues': 0, 'classical': 1, 'country': 2, 'disco': 3, 'hiphop': 4, 'jazz': 5, 'metal': 6, 'pop': 7,
          'reggae': 8, 'rock': 9}
mood = {'energetic': 0, 'romantic': 1, 'sad': 2, 'dramatic': 3, 'happy': 4}
weights_path_genre_classification = 'C:/Users/te200/coursework_ML/Weights/songs_classification.weights.h5'
weights_path_mood_classification = 'C:/Users/te200/coursework_ML/Weights/songs_mood_classification_MobileNet.weights.h5'


def classificate(type, audio_file):
    if type == 'by genre':
        shape = (-1, 64, 173, 1)
        model_ = Model_Genre_Classification(weights=weights_path_genre_classification, input_shape=(64, 173, 1),
                                            output_shape=(10))
        n_mels = 64
        dict_ = genres
    elif type == 'by mood':
        shape = (-1, 128, 173, 1)
        model_ = Model_Mood_Classification(weights=weights_path_mood_classification, input_shape=(128, 173, 1),
                                           output_shape=(5))
        n_mels = 128
        dict_ = mood

    y, sr = librosa.load(
        audio_file, mono=True, duration=2)
    ps = librosa.feature.melspectrogram(y=y, sr=sr, hop_length=256, n_fft=512, n_mels=n_mels)
    ps = librosa.power_to_db(ps ** 2)
    ps = ps.reshape(shape)
    predict = model_.predict(ps)
    predict = predict.squeeze()
    y_full, sr_full = librosa.load(
        audio_file, mono=True)
    duration = librosa.get_duration(y=y_full, sr=sr_full)
    steps = int(duration // 2)
    for index in range(1, steps, 3):
        y, sr = librosa.load(
            audio_file, mono=True, duration=2, offset=index * 2)
        ps = librosa.feature.melspectrogram(y=y, sr=sr, hop_length=256, n_fft=512, n_mels=n_mels)
        ps = librosa.power_to_db(ps ** 2)
        ps = ps.reshape(shape)
        predict = [x + y for x, y in zip(model_.predict(ps).squeeze(), predict)]
    total = sum(predict)
    values = dict(zip(dict_.keys(), (predict / total)))
    values = dict(sorted(values.items(), key=lambda item: item[1]))
    return values


# RECOGNITION PART

from recognition import compute_spectrogram, compute_constellation_map, constellation_map, compare, hash

hashes = pd.read_csv('C:/Users/te200/coursework_ML/hash_for_recognition.csv', index_col='Unnamed: 0')


def recognize(path):
    """Recognition of song
    Args:
        path (str): path to music in .wav format (Default value = 'random.wav')
        dist_freq (int): Neighborhood parameter for frequency direction (kappa) (Default value = 2)
        dist_time (int): Neighborhood parameter for time direction (tau) (Default value = 2)
        offset (int): place of song from which we start load (Default = 0)

    Returns:
        name (str):  name of recognized song
    """
    print(path)
    spec = compute_spectrogram(path, duration=3, offset=0)
    Cmap = compute_constellation_map(spec, dist_freq=2, dist_time=2)
    k_test, n_test = constellation_map(Cmap, np.log(1 + 1 * spec))
    test = hash(k_test, n_test)
    test = list(map(str, test))
    max = -1
    name = ''
    for idx in range(len(hashes)):
        if max < compare(test, hashes.values[idx].flatten().tolist()):
            name = hashes.index[idx]
            max = compare(test, hashes.values[idx].flatten().tolist())
            print(max, name)

    return name.replace('songs/songs_wav/', '').replace('.wav', '')


# INTERFACE INITIALIZATION

io1 = gr.Interface(recommend_songs, title="Recommendation", inputs = [gr.Textbox(placeholder="name, year"), gr.Slider(3, 50, step=1)], outputs= gr.DataFrame(), examples= [[names[i] + ', ' + str(years[i])] + [random.randint(3, 50)]  for i in range(len(df))])
io2 = gr.Interface(
    fn=classificate,
    title="Classification",
    description="Upload an audio clip, and let AI do the hard work of classification",
    inputs=[gr.Radio(["by genre", "by mood"], label="Type of classification", info="Select how to classificate a song"),
            gr.Audio(label="Upload Audio File", type='filepath')],
    outputs=gr.Label(),
)

io3 = gr.Interface(
    fn=recognize,
    title="Recognition",
    description="Upload an audio clip, and let AI do the hard work of recognition",
    inputs=gr.Audio(label="Upload Audio File", type='filepath'),
    outputs="text",
)

gr.TabbedInterface(
    [io1, io2, io3], ["Recommendation", 'Music classification', 'Song recognition']
).launch()
