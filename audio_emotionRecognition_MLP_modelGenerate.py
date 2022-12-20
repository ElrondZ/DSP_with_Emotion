import librosa
import soundfile
import os
import glob
import pickle
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

emotionList = {'01': 'neutral', '02': 'calm', '03': 'happy', '04': 'sad',
               '05': 'angry', '06': 'fearful', '07': 'disgust', '08': 'surprised'}
chosen_emotions = ['calm', 'happy', 'fearful', 'disgust']


def load_dataset(test_size=0.2):
    x, y = [], []
    for file in glob.glob("./AudioDataSet/Actor_*/*.wav"):
        file_name = os.path.basename(file)
        emotion = emotionList[file_name.split("-")[2]]
        if emotion not in chosen_emotions:
            continue
        feature = feature_extraction(file, mfcc=True, chroma=True, mel=True)
        x.append(feature)
        y.append(emotion)
    return train_test_split(np.array(x), y, test_size=test_size, random_state=9)


def feature_extraction(file_name, mfcc, chroma, mel):
    with soundfile.SoundFile(file_name) as sound_file:
        mySoundFile = sound_file.read(dtype="float32")
        sample_rate = sound_file.samplerate
        result = mfcc_method(mfcc, chroma, mel, sample_rate, mySoundFile)
    return result


def mfcc_method(mfcc, chroma, mel, sample_rate, mySoundFile):
    if chroma:
        stft = np.abs(librosa.stft(mySoundFile))
    result = np.array([])
    if mfcc:
        mfccs = np.mean(librosa.feature.mfcc(y=mySoundFile, sr=sample_rate, n_mfcc=40).T, axis=0)
        result = np.hstack((result, mfccs))
    if chroma:
        chroma = np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T, axis=0)
        result = np.hstack((result, chroma))
    if mel:
        mel = np.mean(librosa.feature.melspectrogram(mySoundFile, sr=sample_rate).T, axis=0)
        result = np.hstack((result, mel))
    return result


def training_model():
    x_train, x_test, y_train, y_test = load_dataset(test_size=0.2)

    model = MLPClassifier(alpha=0.01, batch_size=256, epsilon=1e-08, hidden_layer_sizes=(300,),
                          learning_rate='adaptive',
                          max_iter=500)

    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)
    accuracy = accuracy_score(y_true=y_test, y_pred=y_pred)
    print("Accuracy: {:.2f}%".format(accuracy * 100))
    return model


def save_model(model):
    filename = 'model/audioModel/audio_MLP_model.pkl'
    pickle.dump(model, open(filename, 'wb'))


if __name__ == "__main__":
    mlp_model = training_model()
    save_model(mlp_model)
