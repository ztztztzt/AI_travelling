import cv2
import os
import matplotlib.pyplot as plt  
from PIL import Image
import uploadimage as upimg

'''
img = Image.open('18.jpg') # image exten	sion *.png,*.jpg
new_width  = 50
new_height = 50
img = img.resize((new_width, new_height), Image.ANTIALIAS)
img.save('output image name.png') # format may what u want ,*.png,*jpg,*.gif
'''

color = (0,0,255)       # reverse of RGB (B,G,R) - weird
strokeWeight = 1  
new_path = '/home/t28/Documents/ve450/AI_travelling/demo/final'

number = 0

folder = '/home/t28/Documents/ve450/AI_travelling/demo/users'
List = os.listdir(folder)
for i in range(len(List)):
	number = number + 1
	img_name = List[i]
	img_name = folder + '/' + img_name
	img = cv2.imread(img_name)

	faces = upimg.getrect(img_name)

	if not faces is (): 
		y = faces['y']
		x = faces['x']
		w = faces['w']
		h = faces['h']
		roiImg = img[y:y+w,x:x+h]

		new_name = new_path+'/' + str(number)+'.jpg'
		cv2.imwrite(new_name,roiImg)
		cv2.rectangle(img,(x,y),(x+h,y+w),(0,0,255),2)

		img = Image.open(new_name) # image exten	sion *.png,*.jpg
		new_width  = 50
		new_height = 50
		img = img.resize((new_width, new_height), Image.ANTIALIAS)
		img.save(new_name) # format may what u want ,*.png,*jpg,*.gif

