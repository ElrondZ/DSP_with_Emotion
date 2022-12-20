import tkinter
from tkinter import *
from PIL import ImageTk, Image
import video_emotionRecognition_control
import tkinter as tk
import audio_emotionRecognition_control
import matplotlib as mpl
from tkinter import Tk, Frame
import cv2
import dlib
import numpy as np


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
    # my_emotion_recognition = video_emotionRecognition_control.EmotionRecognition_Video()
    # my_emotion_recognition.face_and_emotion_recognition()


    # Using the face detector and predictor which provided by dlib
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("./model/videoModel/shape_predictor_68_face_landmarks.dat")

    # Using the camera of the computer
    cap = cv2.VideoCapture(0)
    cap.set(3, 480)

    # Screenshot Count Index
    screenshotCount = 0

    # Initialize Eyebrow Data List
    eyebrow_list_x = []
    eyebrow_list_y = []

    while cap.isOpened():

        # Read the video frame by frame
        flag, frame_read = cap.read()
        k = cv2.waitKey(1)

        # Detect the number of faces
        img_gray = cv2.cvtColor(frame_read, cv2.COLOR_RGB2GRAY)
        numOfFaces = detector(img_gray, 0)

        if (len(numOfFaces) != 0):

            for i in range(len(numOfFaces)):

                for k, d in enumerate(numOfFaces):

                    # Annotate the location of the face
                    cv2.rectangle(frame_read, (d.left(), d.top()), (d.right(), d.bottom()), (0, 0, 255))

                    # Get the face recognition frame
                    face_width = d.right() - d.left()
                    shape = predictor(frame_read, d)

                    # Show Feature Points
                    for i in range(68):
                        cv2.circle(frame_read, (shape.part(i).x, shape.part(i).y), 5, (0, 255, 0), -1, 8)
                        cv2.putText(frame_read, str(i), (shape.part(i).x, shape.part(i).y), cv2.FONT_HERSHEY_SIMPLEX,
                                    0.5, (255, 255, 255))

                    # Analyze how open the mouth is
                    mouth_width = (shape.part(54).x - shape.part(48).x) / face_width
                    mouth_height = (shape.part(66).y - shape.part(62).y) / face_width

                    # Analyze eyebrow height and distance
                    eyebrow_height = 0
                    eyebrow_distance = 0
                    for j in range(17, 21):
                        eyebrow_height = eyebrow_height + (shape.part(j).y - d.top()) + (shape.part(j + 5).y - d.top())
                        eyebrow_distance = eyebrow_distance + shape.part(j + 5).x - shape.part(j).x
                        eyebrow_list_x.append(shape.part(j).x)
                        eyebrow_list_y.append(shape.part(j).y)

                    # Calculate the slope of the eyebrows
                    eyebrow_point_x = np.array(eyebrow_list_x)
                    eyebrow_point_y = np.array(eyebrow_list_y)
                    z1 = np.polyfit(eyebrow_point_x, eyebrow_point_y, 1)

                    eyebrow_measurement = -round(z1[0], 3)

                    # Analyze how open the eyes are
                    eye_sum = (shape.part(41).y - shape.part(37).y + shape.part(40).y - shape.part(38).y + shape.part(
                        47).y - shape.part(43).y + shape.part(46).y - shape.part(44).y)
                    eye_hight = (eye_sum / 4) / face_width

                    # Analyze sentiment changes based on the above parameters
                    if round(mouth_height >= 0.03):
                        if eye_hight >= 0.056:
                            cv2.putText(frame_read, "Amazing", (d.left(), d.bottom() + 20), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                        (0, 0, 255), 2, 4)

                        else:
                            cv2.putText(frame_read, "Happy", (d.left(), d.bottom() + 20), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                        (0, 0, 255), 2, 4)

                    else:
                        if eyebrow_measurement <= -0.3:
                            cv2.putText(frame_read, "Angry", (d.left(), d.bottom() + 20), cv2.FONT_HERSHEY_SIMPLEX, 2,
                                        (0, 0, 255), 3, 4)
                        else:
                            cv2.putText(frame_read, "Nature", (d.left(), d.bottom() + 20), cv2.FONT_HERSHEY_SIMPLEX, 2,
                                        (0, 0, 255), 3, 4)
            # Show Faces Number
            cv2.putText(frame_read, "There are " + str(len(numOfFaces)) + " faces in the camera area.", (20, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3, cv2.LINE_AA)
        else:
            # If no face is detected
            cv2.putText(frame_read, "Please put your face in the camera.", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 2,
                        (0, 0, 255), 3, cv2.LINE_AA)

        # Keyboard Instruction
        frame_read = cv2.putText(frame_read, "Press 'S' to save screenshot.", (20, 900), cv2.FONT_HERSHEY_SIMPLEX, 1.5,
                                 (255, 0, 0), 3, cv2.LINE_AA)
        frame_read = cv2.putText(frame_read, "Press 'Q' to quit.", (20, 970), cv2.FONT_HERSHEY_SIMPLEX, 1.5,
                                 (255, 0, 0), 3, cv2.LINE_AA)

        # Press S to save the picture
        if (cv2.waitKey(1) & 0xFF) == ord('s'):
            screenshotCount += 1
            cv2.imwrite("screenshot_test" + str(screenshotCount) + ".jpg", frame_read)

        # Press Q to Quit
        if (cv2.waitKey(1) & 0xFF) == ord('q'):
            break

        cv2.imshow("Video Emotion Recognition", frame_read)

    cap.release()
    cv2.destroyAllWindows()


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
                                     height=1, command=lambda: audio_emotionRecognition_control.displayEmotionResult())

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
