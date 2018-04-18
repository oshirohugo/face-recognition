#!/usr/bin/env python

import cv2
import numpy as np

TRAINNER_PATH = 'trainner/trainner.yml'
MIN_CONFIDENCE = 30
CONSECUTIVE_DETECTION_THRESH = 5
CAMERA_ID = 0

# TODO you should change this according to your data set
USERS = {
    '1': 'Hugo',
    '2': 'Joao',
    '3': 'Artiga',
    '4': 'Gabriel',
    '5': 'Cauli'
}

recognizer = cv2.createLBPHFaceRecognizer()
recognizer.load(TRAINNER_PATH)

CASCADE_PATH = "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(CASCADE_PATH)

cap = cv2.VideoCapture(CAMERA_ID)
font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1)

user_buffer = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.2, 5)

    for(x, y, w, h) in faces:
        cv2.rectangle(frame, (x-50, y-50), (x+w+50, y+h+50), (0, 225, 15), 8)
        # Do the recognition
        user_id, confidence = recognizer.predict(gray[y:y+h, x:x+w])
        user_name = 'Unknown'

        if confidence > MIN_CONFIDENCE:
            user_name = USERS[str(user_id)]

        cv2.cv.PutText(cv2.cv.fromarray(frame),
                       str(user_name), (x, y+h), font, 255)

    # Display the resulting frame
    cv2.imshow('frame', frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

print 'Success'
