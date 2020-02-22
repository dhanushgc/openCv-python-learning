import cv2
import numpy as np
import matplotlib.pyplot as plt
#                         0 = IMREAD_GRAYSCALE
img = cv2.imread('img.jpg',0)
#cv2.IMREAD_COLOR = 1
#cv2.IMREAD_UNCHANGED = -1

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#matplotlib 
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.plot([50,100],[80,100],'c',linewidth=5)
plt.show()





