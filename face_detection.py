import cv2
import matplotlib.pyplot as plt  

# rectangle color and stroke
color = (0,0,255)       # reverse of RGB (B,G,R) - weird
strokeWeight = 1        # thickness of outline

# set window name
windowName = "Object Detection"

# load an image to search for faces
img = cv2.imread("5.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# load detection file (various files for different views and uses)
facecascade = cv2.CascadeClassifier("/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml")



# preprocessing, as suggested by: http://www.bytefish.de/wiki/opencv/object_detection

# detect objects, return as list
faces = facecascade.detectMultiScale(gray) 


    # get a list of rectangles
for x,y, width,height in faces:
    cv2.rectangle(img, (x,y), (x+width, y+height), color, strokeWeight)

# display!
cv2.imshow(windowName, img)
