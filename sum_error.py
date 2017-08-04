import cv2
import os
import matplotlib.pyplot as plt  
import uploadimage as upimg

total = 0
number = 0 #Total number of error pictures
folder = '/home/t28/Documents/ve450/noface_total'
List = os.listdir(folder)
save_path = '/home/t28/Documents/ve450/error_set'
for i in range(len(List)):
	name1 = List[i]
	new_folder = os.path.join(folder,name1)
	new_list = os.listdir(new_folder)
	for j in range(len(new_list)):
		sub_folder = new_list[j]
		directory = os.path.join(new_folder,sub_folder)
		sub_list = os.listdir(directory)
		for k in range(len(sub_list)):
			total = total + 1
			if total % 10 == 0:
				print total
			img = sub_list[k]
			img_name = os.path.join(directory,img)
			img = cv2.imread(img_name)
			faces = upimg.getrect(img_name)
			if faces == -1:   ## No Face
				pass
			else:
				y = faces['y']
				x = faces['x']
				w = faces['w']
				h = faces['h']
				roiImg = img[y:y+w,x:x+h]
				number = number + 1
				new_name = save_path + '/' + str(number) + '.jpg'
				cv2.rectangle(img,(x,y),(x+h,y+w),(0,0,255),3)
				cv2.imwrite(new_name,img)


