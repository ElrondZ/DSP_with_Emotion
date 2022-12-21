'''
@Project ：Emotion Recognition based on Video and Audio
@File    ：video_emotionRecognition_control.py
@Author  ：Zihan Zeng
@Date    ：12/02/2022
'''

import cv2
import dlib
import numpy as np


def analyzeSentiment(frame_read, mouth_height, eyebrow_measurement, eye_hight, different_face):
    """

    Analyze sentiment changes based on the parameters

    :param frame_read:              Frames
    :param mouth_height:            The height of the mouth
    :param eyebrow_measurement:     Measurement about eyebrows
    :param eye_hight:               The distance at which the eye position changes
    :param different_face:          Faces
    :return:
    """
    if round(mouth_height >= 0.027):
        if eye_hight >= 0.049:
            cv2.putText(frame_read, "Amazing", (different_face.left(), different_face.bottom() + 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, 4)

        else:
            cv2.putText(frame_read, "Happy", (different_face.left(), different_face.bottom() + 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, 4)

    else:
        if eyebrow_measurement <= -0.28:
            cv2.putText(frame_read, "Angry", (different_face.left(), different_face.bottom() + 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3, 4)
        else:
            cv2.putText(frame_read, "Nature", (different_face.left(), different_face.bottom() + 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3, 4)


def caluculateFeaturePoints(frame_read, shape, face_width, eyebrow_list_x, eyebrow_list_y, different_face):
    '''

    Draw Feature Points and calculate important parameters

    :param frame_read:          Frames
    :param shape:               Predictor
    :param face_width:          Width of the face
    :param eyebrow_list_x:      Eyebrow One
    :param eyebrow_list_y:      Right Two
    :param different_face:      Faces
    :return:
    '''
    # Show Feature Points
    for i in range(68):
        cv2.circle(frame_read, (shape.part(i).x, shape.part(i).y), 5, (0, 255, 0), -1, 8)
        cv2.putText(frame_read, str(i), (shape.part(i).x, shape.part(i).y), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (255, 255, 255))

    # Analyze Mouth
    mouth_width = (shape.part(54).x - shape.part(48).x) / face_width
    mouth_height = (shape.part(66).y - shape.part(62).y) / face_width

    # Analyze Eyebrows
    eyebrow_height = 0
    eyebrow_distance = 0

    for flag in range(17, 21):
        eyebrow_height = eyebrow_height + (shape.part(flag).y - different_face.top()) + (
                    shape.part(flag + 5).y - different_face.top())
        eyebrow_distance = eyebrow_distance + shape.part(flag + 5).x - shape.part(flag).x

        eyebrow_list_x.append(shape.part(flag).x)
        eyebrow_list_y.append(shape.part(flag).y)

    # Calculate the slope of the Eyebrows
    eyebrow_point_x = np.array(eyebrow_list_x)
    eyebrow_point_y = np.array(eyebrow_list_y)
    z1 = np.polyfit(eyebrow_point_x, eyebrow_point_y, 1)

    eyebrow_measurement = -round(z1[0], 3)

    # Analyze Eyes
    eye_sum = (shape.part(41).y - shape.part(37).y + shape.part(40).y - shape.part(38).y + shape.part(
        47).y - shape.part(43).y + shape.part(46).y - shape.part(44).y)
    eye_hight = (eye_sum / 4) / face_width

    analyzeSentiment(frame_read, mouth_height, eyebrow_measurement, eye_hight, different_face)


def ifHasFaces(numOfFaces, frame_read, predictor, eyebrow_list_x, eyebrow_list_y):
    '''

    If detect faces, then begin to analyze.

    :param numOfFaces:          Number of faces
    :param frame_read:          Frames
    :param predictor:           The predictor from dlib
    :param eyebrow_list_x:      The x point of the eyebrow
    :param eyebrow_list_y:      The y point of the eyebrow
    :return:
    '''
    if len(numOfFaces) != 0:
        for i in range(len(numOfFaces)):
            for index, different_face in enumerate(numOfFaces):
                # Annotate the location of the face
                cv2.rectangle(frame_read, (different_face.left(), different_face.top()),
                              (different_face.right(), different_face.bottom()), (0, 0, 255))

                # Get the face recognition frame
                face_width = different_face.right() - different_face.left()
                shape = predictor(frame_read, different_face)

                caluculateFeaturePoints(frame_read, shape, face_width, eyebrow_list_x, eyebrow_list_y, different_face)

        # Show Faces Number
        cv2.putText(frame_read, "There are " + str(len(numOfFaces)) + " faces in the camera area.", (20, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3, cv2.LINE_AA)
    else:
        # If no face is detected
        cv2.putText(frame_read, "Please put your face in the camera.", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 2,
                    (0, 0, 255), 3, cv2.LINE_AA)


def openVideo(mycamera, detector, predictor, eyebrow_list_x, eyebrow_list_y, screenshotCount):
    '''

    Open the camera and prepare to use the video to analyze.

    :param mycamera:            Computer's camera
    :param detector:            Detector from dlib
    :param predictor:           predictor from dlib
    :param eyebrow_list_x:      The x point of the eyebrow
    :param eyebrow_list_y:      The y point of the eyebrow
    :param screenshotCount:
    :return:
    '''
    while mycamera.isOpened():

        # Read the video frame by frame
        flag, frame_read = mycamera.read()
        k = cv2.waitKey(1)

        # Detect the number of faces
        img_gray = cv2.cvtColor(frame_read, cv2.COLOR_RGB2GRAY)
        numOfFaces = detector(img_gray, 0)

        ifHasFaces(numOfFaces, frame_read, predictor, eyebrow_list_x, eyebrow_list_y)

        # Keyboard Instruction
        frame_read = cv2.putText(frame_read, "Press 'S' to save screenshot.", (20, 900), cv2.FONT_HERSHEY_SIMPLEX, 1.5,
                                 (255, 0, 0), 3, cv2.LINE_AA)
        frame_read = cv2.putText(frame_read, "Press 'Q' to quit.", (20, 970), cv2.FONT_HERSHEY_SIMPLEX, 1.5,
                                 (255, 0, 0), 3, cv2.LINE_AA)

        if (cv2.waitKey(1) & 0xFF) == ord('s'):
            screenshotCount += 1
            cv2.imwrite("screenshot_test" + str(screenshotCount) + ".jpg", frame_read)
        if (cv2.waitKey(1) & 0xFF) == ord('q'):
            break

        cv2.imshow("Video Emotion Recognition", frame_read)


def openVideoEmotionRecognition():
    '''

    Prepare to be called in mainControlWindow.

    :return:
    '''
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("./model/videoModel/shape_predictor_68_face_landmarks.dat")

    # Screenshot Count Index
    screenshotCount = 0

    # Using the camera of the computer
    mycamera = cv2.VideoCapture(0)
    mycamera.set(3, 480)

    # Initialize Eyebrow Data List
    eyebrow_list_x = []
    eyebrow_list_y = []

    openVideo(mycamera, detector, predictor, eyebrow_list_x, eyebrow_list_y, screenshotCount)

    mycamera.release()
    cv2.destroyAllWindows()
