import cv2
import numpy as np

img = cv2.imread('Screenshot2.png')
imgCanny = cv2.Canny(img,150,200)

kernel = np.ones((5,5),np.uint8)

imgDilation = cv2.dilate(imgCanny,kernel,iterations=1)

imgErosion = cv2.erode(imgDilation,kernel,iterations=1)

#cv2.imshow('Canny Image',imgCanny)
#cv2.imshow('Dilation Image',imgDilation)
cv2.imshow('Erosion Image',imgErosion)

cv2.waitKey(0)
cv2.destroyAllWindows()