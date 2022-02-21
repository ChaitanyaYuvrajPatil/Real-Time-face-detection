import cv2
import numpy as np
img = cv2.imread('Screenshot2.png')

img_Resize = cv2.resize(img,(500,500))
imgHor = np.hstack((img_Resize,img_Resize)) #For Horizontal
imgVer = np.vstack((img_Resize,img_Resize)) #For Vertical
cv2.imshow("Horizontal",imgHor)

cv2.waitKey(0)
cv2.destroyAllWindows()
