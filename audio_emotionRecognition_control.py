import tkinter as tk
from tkinter import messagebox
import librosa
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from PIL import ImageTk, Image


# wrng GRF，变量名用拼音的？button的文字用中文的？注释用中文的？
# wrng GRF，变量名用拼音的？button的文字用中文的？注释用中文的？
# wrng GRF，变量名用拼音的？button的文字用中文的？注释用中文的？
# wrng GRF，变量名用拼音的？button的文字用中文的？注释用中文的？
# wrng GRF，变量名用拼音的？button的文字用中文的？注释用中文的？
# wrng GRF，变量名用拼音的？button的文字用中文的？注释用中文的？
# wrng GRF，变量名用拼音的？button的文字用中文的？注释用中文的？
# wrng GRF，变量名用拼音的？button的文字用中文的？注释用中文的？

# ndy GRF, 你难道没发现你的变量名跟函数名字是一样的？？？？？？？？？？？？？？？？？？？？？？
# ndy GRF, 你难道没发现你的变量名跟函数名字是一样的？？？？？？？？？？？？？？？？？？？？？？
# ndy GRF, 你难道没发现你的变量名跟函数名字是一样的？？？？？？？？？？？？？？？？？？？？？？
# ndy GRF, 你难道没发现你的变量名跟函数名字是一样的？？？？？？？？？？？？？？？？？？？？？？
# ndy GRF, 你难道没发现你的变量名跟函数名字是一样的？？？？？？？？？？？？？？？？？？？？？？
# ndy GRF, 你难道没发现你的变量名跟函数名字是一样的？？？？？？？？？？？？？？？？？？？？？？
# ndy GRF, 你难道没发现你的变量名跟函数名字是一样的？？？？？？？？？？？？？？？？？？？？？？
# ndy GRF, 你难道没发现你的变量名跟函数名字是一样的？？？？？？？？？？？？？？？？？？？？？？
# ndy GRF, 你难道没发现你的变量名跟函数名字是一样的？？？？？？？？？？？？？？？？？？？？？？
# ndy GRF, 你难道没发现你的变量名跟函数名字是一样的？？？？？？？？？？？？？？？？？？？？？？




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


def take_audio():
    print("aaa")


def pinpu():
    print("频谱")


def boxingtu():
    print("波形图")


def result():
    print("情感结果")


root = tk.Tk()

# Window Title
root.title("Audio Emotion Recognition")

# Window Size
root.minsize(600, 400)

# Set Somponents
get_title_image = Image.open("./UI_Resources/emotion.jpg")
title_img = ImageTk.PhotoImage(get_title_image)
my_title_image = tk.Label(root, image=title_img)

################# 你没有发现只要你运行整个文件，就会直接运行command里的函数吗，前面加lamda: ，就改成了点击才会运行这个函数
button_recording = tk.Button(root, text='Record Your Voice', font=('Roman', 20), width=30, height=1, command=lambda: take_audio())
button_waveform = tk.Button(root, text='Generate Wave Form', font=('Roman', 20), width=30, height=1,
                     command=lambda: boxingtu())
button_spectrogram = tk.Button(root, text='Generate Spectrogram', font=('Roman', 20), width=30, height=1, command=lambda: pinpu())
button_emotionResult = tk.Button(root, text='Generate Emotion Recognition Result', font=('Roman', 20), width=30, height=1,
                   command=lambda: displayEmotionResult())

# Display Components
my_title_image.pack()
button_recording.place(relx=0.17, rely=0.57)
button_waveform.place(relx=0.17, rely=0.67)
button_spectrogram.place(relx=0.17, rely=0.77)
button_emotionResult.place(relx=0.17, rely=0.87)

root.mainloop()
