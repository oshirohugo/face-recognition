#!/usr/bin/env python

import sys
import cv2


if len(sys.argv) < 3:
    print sys.argv[0] + ' <user-id> <data-set-dir-path>'
    exit(1)

CASCADE_PATH = "haarcascade_frontalface_default.xml"
N_OF_SAMPLES = 500

user_id = sys.argv[1]
data_set_path = sys.argv[2]

cam = cv2.VideoCapture(1)
detector = cv2.CascadeClassifier(CASCADE_PATH)

sample_num = 0

while(True):
	ret, img = cam.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = detector.detectMultiScale(gray, 1.3, 5)
	for (x, y, w, h) in faces:
		cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

	# incrementing sample number
	sample_num = sample_num + 1
	# saving the captured face in the dataset folder
	cv2.imwrite(data_set_path + '/user.' + user_id + '.' + str(sample_num) +
	'.jpg', gray[y:y+h, x:x+w])

	cv2.imshow('frame', img)

	#wait for 100 miliseconds
	if cv2.waitKey(100) & 0xFF == ord('q'):
		break
	# break if the sample number is morethan 20
	elif sample_num > N_OF_SAMPLES:
		break

cam.release()
cv2.destroyAllWindows()

print 'Finish'
