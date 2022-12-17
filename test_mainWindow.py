import tkinter
from tkinter import *
import tkinter as tk
import audio_test

root = Tk()
root.title('Digital Signal Processing Final Project')
root.geometry('1200x600')

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
    print("haha")


def on_button_click(self):
    new_window = tk.Toplevel(self)
    new_window.title('Audio Emotion Recognition')
    new_window.geometry('600x400')
    filename = "record_a_sound.wav"
    filepath = "./" + filename

    button_recording = tk.Button(new_window, text='Record Your Voice', font=('Roman', 20), width=30, height=1,
                                 command=lambda: audio_test.record_sound(filename))
    button_waveform = tk.Button(new_window, text='Generate Wave Form', font=('Roman', 20), width=30, height=1,
                                command=lambda: audio_test.displayWaveform(filepath))
    button_spectrogram = tk.Button(new_window, text='Generate Spectrogram', font=('Roman', 20), width=30, height=1,
                                   command=lambda: audio_test.displaySpectrogram(filepath))
    button_emotionResult = tk.Button(new_window, text='Generate Emotion Recognition Result', font=('Roman', 20), width=30,
                                     height=1, command=lambda: audio_test.displayEmotionResult())

    button_recording.place(relx=0.17, rely=0.57)
    button_waveform.place(relx=0.17, rely=0.67)
    button_spectrogram.place(relx=0.17, rely=0.77)
    button_emotionResult.place(relx=0.17, rely=0.87)

    root.mainloop()


button_video = Button(root, text='Video Emotion Recognition', font=('Roman', 20), command=lambda:openVideoEmotionRecognition())
button_audio = Button(root, text='Audio Emotion Recognition', font=('Roman', 20), command=lambda:on_button_click(root))

button_video.place(relx=0.15, rely=0.7, relwidth=0.23, relheight=0.1)
button_audio.place(relx=0.65, rely=0.7, relwidth=0.23, relheight=0.1)
text_subjectTitle.pack()
text_author.pack()
root.mainloop()
