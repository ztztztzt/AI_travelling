import requests
import hashlib
import json
import urllib2
import base64
import os
import get_session_id as gid


folder = '/home/t28/Pictures/Webcam'
List = os.listdir(folder)
for i in range(len(List)):
	img = List[i]
	img_name = os.path.join(folder,img)
	f = open(img_name,'rb')
	f_64 = base64.b64encode(f.read())

	data = {"repository_id" : 14, "picture_image_content_base64":f_64,"external_id": f_64,"name":"first_try"}
	r = urllib2.Request("http://127.0.0.1:9100/face/v1/framework/face_image/repository/picture/synchronized",headers={"session_id": id},data=json.dumps(data))
	response = urllib2.urlopen(r)
	r = response.read()
	final = json.loads(r)