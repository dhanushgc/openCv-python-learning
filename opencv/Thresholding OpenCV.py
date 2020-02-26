import cv2
import numpy as np

img = cv2.imread('bookpage.jpg')
grayscale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

retval, threshold = cv2.threshold(img,12,255,cv2.THRESH_BINARY)
retval2, threshold2 = cv2.threshold(grayscale,12,255,cv2.THRESH_BINARY)
th = cv2.adaptiveThreshold(grayscale,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)

cv2.imshow('original',img)
cv2.imshow('threshold',threshold)
cv2.imshow('threshold2',threshold2)
cv2.imshow('adaptive',th)

cv2.waitKey(0)
cv2.destroyAllWindows()
