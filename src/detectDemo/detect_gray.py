# coding: utf-8

import cv2
import numpy as np
import sys

img = cv2.imread("./testImages/testFile2.jpg")
emptyImage = np.zeros(img.shape, np.uint8)  

emptyImage2 = img.copy()  

emptyImage3=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  

cv2.imshow("EmptyImage3", emptyImage3)  
cv2.waitKey (0)  
cv2.destroyAllWindows()  