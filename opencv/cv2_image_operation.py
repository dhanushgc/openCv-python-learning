import numpy as np
import cv2

img = cv2.imread('img.jpg', cv2.IMREAD_COLOR)

#change pixel value
img[55,55] = [255,255,255]
px = img[55,55]
print(px)
#img[100:150,100:150] = [255,255,255]
px = img[100:150,100:150]
print(px)


print(img.shape)
print(img.size)
print(img.dtype)

#roi-region of image
watch_face = img[100:150,100:150]
img[0:50,0:50] = watch_face

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
