import cv2
import dlib
import numpy as np
import nose
import ear
import window
import os


cap = cv2.VideoCapture(0)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("../models/shape_predictor_68_face_landmarks.dat")

wd = window.Window(cv2.imread("../images/others/gray_background.jpg"))


while True:
    _, frame = cap.read()
    #detector and predictor is faster on a gray frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = detector(gray)

    for face in faces:
        landmark = predictor(gray, face)
        parts = landmark.parts()

        ear.update_ear_position(face.right()-face.left(), (face.left(), face.top()), frame, cv2.imread("../images/ears/"+os.listdir("../images/ears")[wd.ear_selected]), frame)

        nose_width = int((parts[35].x - parts[31].x)*2)
        nose.update_nose_position(nose_width,(int((parts[31].x+parts[35].x)/2 - (nose_width/2)), parts[29].y),frame, cv2.imread("../images/noses/"+os.listdir("../images/noses")[wd.nose_selected]), frame)

    wd.show("Window", frame)

    cv2.setMouseCallback("Window", wd.test)

    #end condition
    key = cv2.waitKey(1)
    if key == 27:
        break
