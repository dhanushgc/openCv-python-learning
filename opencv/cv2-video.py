import numpy as np
import cv2
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)

 
while True:
    ret, frame = cap.read() #returnes frame by frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #converts to gray color
  
    cv2.imshow('frame', gray) #display gray video
    cv2.imshow('video', frame) #displays color video

    if cv2.waitKey(1) & 0xFF == ord('q'):  #if q is pressed exits while loop
        break
# releases webcam and closes imshow() 
cap.release() 
cv2.destroyAllWindows()
