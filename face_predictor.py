#using python code and OpenCV Library
#loading the libraries 
import numpy as np
import cv2
import matplotlib.pyplot as plt
%matplotlib inline
#loading the image 
from google.colab import files
uploaded = files.upload()

from PIL import Image
from io import BytesIO
im = Image.open(BytesIO(uploaded['image.jpeg']))

type(im)     #to see whether it loaded

#Loading the image to be tested
image_1 = cv2.imread(im)

#Converting to grayscale
test_image_gray = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)


# Haar Cascade is a type of pre-trained classifiers 
# The detectMultiscale is a part of the classifier. it returns a rectangle with coordinates(x,y,w,h) 
haar_cascade_face = cv2.CascadeClassifier('data/haarcascade/haarcascade_frontalface_default.xml')
faces_rects = haar_cascade_face.detectMultiScale(test_image_gray, scaleFactor = 1.2, minNeighbors = 5);

# Let us print the no. of faces found
print('Faces found: ', len(faces_rects))
for (x,y,w,h) in faces_rects:
     cv2.rectangle(test_image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
