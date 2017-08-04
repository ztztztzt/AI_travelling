import cv2
import os
import matplotlib.pyplot as plt  


num_total = 0
num_succ = 0

folder = '/home/t28/Documents/ve450/noface/'
List = os.listdir(folder)
imglist = []
for i in range(len(List)):
	name1 = List[i]
	new_folder = os.path.join(folder,name1)
	new_list = os.listdir(new_folder)
	for j in range(len(new_list)):
		image 	= new_list[j]	
		num_total = num_total + 1
		print num_total
		directory = os.path.join(new_folder,image)

# rectangle color 	and stroke
		color = (0,0,255)       # reverse of RGB (B,G,R) - weird
		strokeWeight = 1        # thickness of outline

		# set window name
		windowName = "Object Detection"
		# load an image to search for faces
		img = cv2.imread(directory)
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		# load Detectionn file (various files for different views and uses)
		facecascade = cv2.CascadeClassifier("/home/t28/Documents/ve450/AI_travelling/haarcascade_frontalface_default.xml")

		# detect objects, return as list
		#faces = facecascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=9, minSize=(30,30))	
		faces = facecascade.detectMultiScale(gray)

		if faces != ():	
			num_succ = num_succ + 1

# 66.4

'''

    # get a list of rectangles
for x,y, width,height in faces:
    cv2.rectangle(img, (x,y), (x+width, y+height), color, strokeWeight)

# save 
_path = os.getcwd()
save_path = os.path.join(_path , "selfphotos")
if not os.path.isdir(save_path):
    os.mkdir(save_path)

if not faces is (): 
        for x,y,z,w in faces:
            roiImg = img[y:y+w,x:x+z]
            cv2.imwrite(save_path+'/' + str(i)+'.jpg',roiImg)
            cv2.rectangle(img,(x,y),(x+z,y+w),(0,0,255),2)
            i +=1

# display!
cv2.destroyAllWindows()
cv2.imshow(windowName, img)
'''

_path = os.getcwd()
cv2.imwrite(_path+'/' + '13_1.jpg',img)