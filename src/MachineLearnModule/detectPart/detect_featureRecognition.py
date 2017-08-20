import cv2
import math

im = cv2.cv.LoadImage("./testImages/testFile2.jpg", cv2.cv.CV_LOAD_IMAGE_GRAYSCALE)
im2 = cv2.CloneImage(im)

# Goodfeatureto track algorithm
eigImage = cv2.CreateMat(im.height, im.width, cv2.IPL_DEPTH_32F)
tempImage = cv2.CloneMat(eigImage)
cornerCount = 500
quality = 0.01
minDistance = 10

corners = cv2.GoodFeaturesToTrack(im, eigImage, tempImage, cornerCount, quality, minDistance)

radius = 3
thickness = 2

for (x,y) in corners:
    cv2.Circle(im, (int(x),int(y)), radius, (255,255,255), thickness)

cv2.ShowImage("GoodfeaturesToTrack", im)

#SURF algorithm
hessthresh = 1500 # 400 500
dsize = 0 # 1
layers = 1 # 3 10

keypoints, descriptors = cv2.ExtractSURF(im2, None, cv2.CreateMemStorage(), (dsize, hessthresh, 3, layers))
for ((x, y), laplacian, size, dir, hessian) in keypoints:
    cv2.Circle(im2, (int(x),int(y)), cv2.Round(size/2), (255,255,255), 1)
    x2 = x+((size/2)*math.cos(dir))
    y2 = y+((size/2)*math.sin(dir))
    cv2.Line(im2, (int(x),int(y)), (int(x2),int(y2)), (255,255,255), 1)

cv2.ShowImage("SURF ", im2)

cv2.WaitKey(0)
