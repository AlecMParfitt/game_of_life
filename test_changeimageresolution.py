import cv2 as cv
import numpy as np
# import scipy as sp

from changeimageresolution import changeimagesamplingresolution

# ## remove ", cv.CAP_DSHOW" to use on Mac or Linux
capture = cv.VideoCapture(0, cv.CAP_DSHOW)

while capture.isOpened():
    
    # Capture frame-by-frame
    ret, frame = capture.read()

    # Our operations on the frame come here
    # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame = changeimagesamplingresolution(frame, np.array([600,600]), 'linear')

    cv.imshow('Video', frame)
    
    # key to quit capture
    if cv.waitKey(1) == ord('q'):
        break