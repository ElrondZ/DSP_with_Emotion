import pickle
import tkinter as tk
import librosa
import librosa.display
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pyaudio
import wave
from tkinter import Tk, Frame, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import audio_emotionRecognition_MLP_modelGenerate


def record_sound(filename, self):
    recording = tk.Toplevel(self)
    recording.geometry('400x200')
    alert = tk.Label(recording, text='recording ends', fg='black', font=('Courier', 45), width=70, height=3)
    alert.pack()

    chunk = 1024
    p = pyaudio.PyAudio()
    stream = p.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=44100,
        input=True,
        frames_per_buffer=chunk
    )

    frames = []

    for i in range(0, 44100 // chunk * 5):
        data = stream.read(chunk)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(filename, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    wf.setframerate(44100)
    wf.writeframes(b''.join(frames))
    wf.close()

    recording.mainloop()

# Using librosa to generate waveform and display
def displayWaveform(filepath, self):
    window_wave = tk.Toplevel(self)
    window_wave.geometry('800x750')

    samples, sr = librosa.load(filepath, sr=16000)
    print(len(samples), sr)
    time = np.arange(0, len(samples)) * (1.0 / sr)

    frame = Frame(window_wave)
    fig = plt.figure()
    plt.plot(time, samples)
    plt.title("Wave Form")
    plt.xlabel("Time(Second)")
    plt.ylabel("Amplitude")
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    frame.pack()
    canvas.get_tk_widget().pack()


# Using librosa to generate spectrogram and display
def displaySpectrogram(filepath, self):
    window_spectrum = tk.Toplevel(self)
    window_spectrum.geometry('800x700')
    frame = Frame(window_spectrum)
    fig = plt.figure()

    x, sr = librosa.load(filepath, sr=16000)
    spectrogram = librosa.amplitude_to_db(librosa.stft(x))
    librosa.display.specshow(spectrogram, y_axis='log')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Spectrogram Form')
    plt.xlabel('Time(Second)')
    plt.ylabel('Frequency(HZ)')
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    frame.pack()
    canvas.get_tk_widget().pack()


# Using NN Model to generate emotion results
def displayEmotionResult(filepath, self):
    window_emotion = tk.Toplevel(self)
    window_emotion.geometry('800x300')

    audioModel = pickle.load(file=open("./model/audioModel/audio_MLP_model.pkl", 'rb'))
    testing_sample = audio_emotionRecognition_MLP_modelGenerate.feature_extraction(filepath, mfcc=True, chroma=True, mel=True)
    testing_result = audioModel.predict([testing_sample])

    text_emotion_result_title = tk.Label(window_emotion, text='Your Emotion Result',
          fg='black',
          font=('Roman', 45),
          width=70,
          height=3,
          )

    text_emotion_result = tk.Label(window_emotion, text=testing_result,
                    fg='blue',
                    font=('Script', 30),
                    width=50,
                    height=2,
                    )

    text_emotion_result_title.pack()
    text_emotion_result.pack()

