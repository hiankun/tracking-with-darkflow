'''
use this script to check whether OpenCV's video function works properly.
'''
import cv2
import sys

cap = cv2.VideoCapture(sys.argv[1])
#cap = cv2.VideoCapture(0)

while(cap.isOpened()):
    ret, frame = cap.read()

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
