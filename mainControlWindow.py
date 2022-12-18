import tkinter
from tkinter import *
from PIL import ImageTk, Image
import video_emotionRecognition_control
import tkinter as tk
import audio_emotionRecognition_control
import matplotlib as mpl
from tkinter import Tk, Frame

mpl.use('MacOSX')


root = Tk()
root.title('Digital Signal Processing Final Project')
root.geometry('1200x600')

get_logo_image = Image.open("./UI_Resources/logo.png")
logo_img = ImageTk.PhotoImage(get_logo_image)
logo = tkinter.Label(root, image=logo_img)

text_subjectTitle = Label(root, text='\nEmotion Recognition\n based on Video and Audio',
                          fg='black',
                          font=('Courier', 45),
                          width=70,
                          height=3,
                          )
text_author = Label(root, text='Zihan Zeng(zz3361) && Runfeng Gai(rg4153)',
                    fg='black',
                    font=('Script', 25),
                    width=50,
                    height=2,
                    )


def openVideoEmotionRecognition():
    my_emotion_recognition = video_emotionRecognition_control.EmotionRecognition_Video()
    my_emotion_recognition.face_and_emotion_recognition()


def on_button_click(self):
    new_window = tk.Toplevel(self)
    new_window.title('Audio Emotion Recognition')
    new_window.geometry('600x400')
    # Set Somponents
    get_title_image = Image.open("./UI_Resources/emotion.jpg")
    title_img = ImageTk.PhotoImage(get_title_image)
    my_title_image = tk.Label(new_window, image=title_img)

    filename = "record_a_sound.wav"
    filepath = "./" + filename

    button_recording = tk.Button(new_window, text='Record Your Voice', font=('Roman', 20), width=30, height=1,
                                 command=lambda: audio_emotionRecognition_control.record_sound(filename, new_window))
    button_waveform = tk.Button(new_window, text='Generate Wave Form', font=('Roman', 20), width=30, height=1,
                                command=lambda: audio_emotionRecognition_control.displayWaveform(filepath, new_window))
    button_spectrogram = tk.Button(new_window, text='Generate Spectrogram', font=('Roman', 20), width=30, height=1,
                                   command=lambda: audio_emotionRecognition_control.displaySpectrogram(filepath, new_window))
    button_emotionResult = tk.Button(new_window, text='Generate Emotion Recognition Result', font=('Roman', 20),
                                     width=30,
                                     height=1, command=lambda: audio_emotionRecognition_control.displayEmotionResult(filepath, new_window))

    button_recording.place(relx=0.17, rely=0.57)
    button_waveform.place(relx=0.17, rely=0.67)
    button_spectrogram.place(relx=0.17, rely=0.77)
    button_emotionResult.place(relx=0.17, rely=0.87)

    my_title_image.pack()
    root.mainloop()

button_video = Button(root, text='Video Emotion Recognition', font=('Roman', 20), command=lambda:openVideoEmotionRecognition())
button_audio = Button(root, text='Audio Emotion Recognition', font=('Roman', 20), command=lambda:on_button_click(root))

button_video.place(relx=0.15, rely=0.7, relwidth=0.23, relheight=0.1)
button_audio.place(relx=0.65, rely=0.7, relwidth=0.23, relheight=0.1)
logo.pack()
text_subjectTitle.pack()
text_author.pack()
root.mainloop()
