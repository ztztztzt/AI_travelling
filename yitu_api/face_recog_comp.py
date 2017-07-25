import cv2
import os
import matplotlib.pyplot as plt
import get_session_id as gid
import uploadimage as upimg
import base64

import re  
  
re_digits = re.compile(r'(\d+)')  
  
def emb_numbers(s):  
    pieces=re_digits.split(s)  
    pieces[1::2]=map(int,pieces[1::2])      
    return pieces  
  
def sort_strings_with_emb_numbers(alist):  
    return sorted(alist, key=emb_numbers)  

id = 19  #the id of database
num_total = 0
num_succ = 0

'''

################### Upload ground_truth image and get start_index ###################
folder = '/home/t28/Documents/ve450/FaceRecAcc/GroundTruth'
List = os.listdir(folder)
List = sort_strings_with_emb_numbers(List) 
img_name = folder + '/' + List[0]
start_index = upimg.uploadimage(img_name, id)   # get the start_index of the first image
for i in range(1, len(List)):
	img_name = folder + '/' + List[i]
	upimg.uploadimage(img_name, id)

'''
start_index = 5348024557502464

##################### Test the face recognition accuracy #########################


folder = '/home/t28/Documents/ve450/FaceRecAcc/ToTest'
List = os.listdir(folder)
List = sort_strings_with_emb_numbers(List)
for i in range(len(List)):
	name1 = List[i]
	img_name = folder + '/' + List[i]
	index = upimg.face_match(img_name, id)
	num_total = num_total + 1
	print num_total
	if index - i == start_index:
		num_succ = num_succ + 1

## num_succ = 158