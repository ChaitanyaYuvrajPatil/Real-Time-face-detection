import cv2

img = cv2.imread('Screenshot2.png')

#GrayScale Image
'''imgGray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow('GrayScale Image',imgGray)'''

#Blur Image
imgBlur = cv2.GaussianBlur(img,(21,21),0)
cv2.imshow('Blurred Image',imgBlur)

cv2.waitKey(0)
cv2.destroyAllWindows()