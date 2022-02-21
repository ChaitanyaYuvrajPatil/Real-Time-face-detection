import cv2
import numpy as np

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("friend.jpg")
#img = cv2.resize(img,(1240,640))
imgGray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

faces = faceCascade.detectMultiScale(imgGray,1.1,4)

for(x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    
cv2.imshow("Output",img)
cv2.waitKey(0)
cv2.destroyAllWindows()