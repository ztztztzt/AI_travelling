import requests
import hashlib
import json
import urllib2
import base64
import os
import get_session_id as gid
import uploadimage as ui

data = {"retrieval": {
        "face_image_id": 9222527611924643855,
        "repository_ids": [8],
        "threshold": 38, #仅返回相似度 XX 以上的结果
     },
    "fields": [ "face_image_id", "repository_id"],
    "condition": {
        "gender": 0 
    },
    "order": { "similarity": -1 },  #按相似度倒序
    "start": 0, "limit": 5 #跳过前面 0 个结果, 最多返回 5 个结果
    }


r = urllib2.Request("http://127.0.0.1:9200/face/v1/framework/face/retrieval",
	headers={"session_id": gid.get_id()},data=json.dumps(data))	

response = urllib2.urlopen(r)
r = response.read()
final = json.loads(r)
print final






