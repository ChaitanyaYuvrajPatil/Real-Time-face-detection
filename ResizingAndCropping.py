import cv2
import numpy as np

img = cv2.imread('Screenshot2.png')
print(img.shape)

#Resize image
'''img_resize = cv2.resize(img,(400,400))
cv2.imshow("Original Image",img)
cv2.imshow("Re-sized Image",img_resize)'''

#Cropping Image
'''imgCropped = img[0:200,200:500]
cv2.imshow("Cropped Image",imgCropped)
print(imgCropped.shape)'''

#Shapes and Text
'''img= np.zeros((512,512))
cv2.imshow("O",img)
print(img.shape)'''

#Line
'''img = np.zeros((512,512,3),np.uint8)
cv2.line(img,(0,0),(300,300),(0,255,255),3)
cv2.imshow("O",img)'''

#Ractangle
'''cv2.rectangle(img,(0,0),(500,500),(255,245,255),cv2.FILLED)
cv2.imshow("O",img)'''

#Circle
'''cv2.circle(img,(400,50),30,(0,255,255),cv2.FILLED)
cv2.imshow("O",img)'''

#putText
cv2.putText(img,"Opencv",(500,500),cv2.FONT_HERSHEY_COMPLEX,1,(150,150,0),3)
cv2.imshow("O", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
