import cv2
import  numpy as np

print(cv2.__version__)
img = cv2.imread('Screenshot2.png')
cv2.imshow("Output", img)
#cv2.imwrite('copy_Screenshot.png',img)
cv2.waitKey(0)
cv2.destroyAllWindow()
