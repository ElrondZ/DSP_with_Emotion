import tkinter
from tkinter import *
from PIL import ImageTk, Image
import video_emotionRecognition

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
    my_emotion_recognition = video_emotionRecognition.EmotionRecognition_Video()
    my_emotion_recognition.face_and_emotion_recognition()


button_video = Button(root, text='Video Emotion Recognition', font=('Roman', 20), command=lambda:openVideoEmotionRecognition())
button_audio = Button(root, text='Audio Emotion Recognition', font=('Roman', 20))

button_video.place(relx=0.15, rely=0.7, relwidth=0.23, relheight=0.1)
button_audio.place(relx=0.65, rely=0.7, relwidth=0.23, relheight=0.1)
logo.pack()
text_subjectTitle.pack()
text_author.pack()
root.mainloop()
