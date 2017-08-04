import requests
import hashlib
import json
import urllib2
import base64
import os
import get_session_id as gid
import uploadimage as ui

start = 3940649673949270
end = 3940649673949273

for i in range(start,end):


    data = {"face_image_id": i}


    r = urllib2.Request("http://127.0.0.1:9200/face/v1/framework/face/delete",
    	headers={"session_id": gid.get_id()},data=json.dumps(data))	

    response = urllib2.urlopen(r)
    r = response.read()
    final = json.loads(r)
    print final



##--enable-gpl --enable-libx264 --enable-nonfree --enable-postproc --enable-version3 --enable-shared --enable-pic --extra-cflags=-fPIC