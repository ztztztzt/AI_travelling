import requests
import hashlib
import json
import urllib2
import base64
import os
import get_session_id as gid


if __name__ == "__main__":

	id = gid.get_id()
	cwd = os.getcwd() + '/18.jpg'
	f = open(cwd,'rb')
	f_64 = base64.b64encode(f.read())

	data = {"picture_image_content_base64":f_64,"external_id": f_64,"name":"first_try"}

    r = urllib2.Request("http://127.0.0.1:9100/face/v1/framework/face_image/repository/picture/synchronized",headers={"session_id": id},data=json.dumps(data))
    #print(r.text())
    response = urllib2.urlopen(r)
    r = response.read()
    final = json.loads(r)
    print final