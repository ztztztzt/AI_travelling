#
#
import sys
import cv2
import dlib
from skimage import io
import os
#
detector = dlib.get_frontal_face_detector()
#win = dlib.image_window()

color = (0,255,0)       # parameters for the box::color
strokeWeight = 3        # parameters for the box::thickness of outline




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

		img = io.imread(directory)
		img = img.copy()

		# The 1 in the second argument indicates that we should upsample the image
		# 1 time.  This will make everything bigger and allow us to detect more
		# faces.
		dets = detector(img, 1)
		if (len(dets) > 0):
			num_succ = num_succ + 1


		'''
		print("Number of faces detected: {}".format(len(dets)))


		for i, d in enumerate(dets):
		    print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
		        i, d.left(), d.top(), d.right(), d.bottom()))
		    cv2.rectangle(img,(d.left(),d.top()),(d.right(),d.bottom()),color,strokeWeight)

		io.imsave("newImg.jpg",img)
		print("image with boxed face saved!")
        
# Finally, if you really want to you can ask the detector to tell you the score
# for each detection.  The score is bigger for more confident detections.
# The third argument to run is an optional adjustment to the detection threshold,
# where a negative value will return more detections and a positive value fewer.
# Also, the idx tells you which of the face sub-detectors matched.  This can be
# used to broadly identify faces in different orientations.

# if (len(sys.argv[1:]) > 0):
#     img = io.imread(sys.argv[1])
		dets, scores, idx = detector.run(img, 1, -1)
		for i, d in enumerate(dets):
		    print("Detection {}, score: {}, face_type:{}".format(
		        d, scores[i], idx[i]))

'''
#%63.56