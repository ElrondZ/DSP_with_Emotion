from tkinter import messagebox
import librosa
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from PIL import ImageTk, Image
import pyaudio
import wave


def record_sound(filename):
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


# Using librosa to generate waveform and display
def displayWaveform():
    ################# 这个地方写的是用来读取静态文件然后显示波形图，你得改成录音完之后，直接传过来导入这个函数里面，下面那个函数一样
    samples, sr = librosa.load(r'your wav file path', sr=16000)

    print(len(samples), sr)
    time = np.arange(0, len(samples)) * (1.0 / sr)

    plt.plot(time, samples)
    plt.title("Wave Form")
    plt.xlabel("Time(Second)")
    plt.ylabel("Amplitude")
    plt.show()


# Using librosa to generate spectrogram and display
def displaySpectrogram():
    x, sr = librosa.load(r'your wav file path', sr=16000)

    spectrogram = librosa.amplitude_to_db(librosa.stft(x))

    librosa.display.specshow(spectrogram, y_axis='log')
    plt.colorbar(format='%+2.0f dB')
    plt.title('Spectrogram Form')
    plt.xlabel('Time(Second)')
    plt.ylabel('Frequency(HZ)')
    plt.show()


# Using NN Model to generate emotion results
def displayEmotionResult():
    showMessageBox("Ongoing")


# Using messagebox to show message in a new window
################# 你可以用这个messagebox解决跳出信息的问题，比如没有录音直接点击查看图，就会跳出请录音
def showMessageBox(myMessage):
    messagebox.showinfo(myMessage)


