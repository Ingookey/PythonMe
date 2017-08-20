# coding: utf-8
# import library - MUST use cv2 if using opencv_traincascade
import cv2

# rectangle color and stroke
color = (0,0,255)       # reverse of RGB (B,G,R) - weird
strokeWeight = 1        # thickness of outline

# set window name
windowName = "Faces Detection"

# load an image to search for faces
image = cv2.imread("./testImages/testFile.jpg")

# load detection file (various files for different views and uses)
cascade = cv2.CascadeClassifier("./xmls/haarcascade_frontalface_alt.xml")

img_copy = cv2.resize(image, (int(image.shape[1]/2), int(image.shape[0]/2)))
gray = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)
gray = cv2.equalizeHist(gray)

# detect objects, return as list
rects = cascade.detectMultiScale(image)

# display until escape key is hit
while True:
    # get a list of rectangles
    for x,y, width,height in rects:
        cv2.rectangle(image, (x,y), (x+width, y+height), color, strokeWeight)

    # display!
    cv2.imshow(windowName, image)

    # escape key (ASCII 27) closes window
    if cv2.waitKey(20) == 27:
        break

# if esc key is hit, quit!
exit()
