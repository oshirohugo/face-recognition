#!/usr/bin/env python

import sys
import cv2
import os
import numpy as np

if len(sys.argv) < 3:
    print sys.argv[0] + ' <data-set-dir-path> <trainner-dir-path>'
    exit(1)

CASCADE_PATH = "haarcascade_frontalface_default.xml"

def get_imgs_and_labels(dataset_path):
    # get the path of all the files in the folder
    img_paths = [os.path.join(dataset_path, f)
                 for f in os.listdir(dataset_path)]
    # create empth face list
    face_samples = []
    # create empty ID list
    img_ids = []
    # now looping through all the image paths and loading the Ids and the images
    for img_path in img_paths:
        # loading the image and converting it to gray scale
        img = cv2.imread(img_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Now we are converting the PIL image into numpy array
        image_np = np.array(gray, 'uint8')
        # getting the Id from the image
        img_id = int(os.path.split(img_path)[-1].split(".")[1])
        face_samples.append(image_np)
        img_ids.append(img_id)
    return face_samples, img_ids


data_set_path = sys.argv[1]
trainner_set_path = sys.argv[2]

recognizer = cv2.createLBPHFaceRecognizer()

faces, ids = get_imgs_and_labels(data_set_path)
recognizer.train(faces, np.array(ids))
recognizer.save(trainner_set_path + '/trainner.yml')
