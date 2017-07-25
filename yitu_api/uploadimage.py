import requests
import hashlib
import json
import urllib2
import base64
import os
import get_session_id as gid



def getrect(img):
    f = open(img,'rb')
    f_64 = base64.b64encode(f.read())

    data = {"picture_image_content_base64":f_64,"external_id": f_64,"name":"first_try"}
    r = urllib2.Request("http://127.0.0.1:9100/face/v1/framework/face_image/repository/picture/synchronized",headers={"session_id": id},data=json.dumps(data))
    response = urllib2.urlopen(r)
    r = response.read()
    final = json.loads(r)
    result = final['results'][0]
    return result['face_rect']


def uploadimage(img, id):
    f = open(img,'rb')
    f_64 = base64.b64encode(f.read())

    data = {"repository_id" : id, "picture_image_content_base64":f_64,"external_id": f_64,"name":"first_try"}
    r = urllib2.Request("http://127.0.0.1:9100/face/v1/framework/face_image/repository/picture/synchronized",headers={"session_id": id},data=json.dumps(data))
    response = urllib2.urlopen(r)
    r = response.read()
    final = json.loads(r)
    result = final['results'][0]
    return result['face_image_id']


def face_match(img, id):
    f = open(img,'rb')
    f_64 = base64.b64encode(f.read())
    data = {"picture_image_content_base64":f_64,"external_id": f_64,"name":"first_try"}
    r = urllib2.Request("http://127.0.0.1:9100/face/v1/framework/face_image/repository/picture/synchronized",headers={"session_id": id},data=json.dumps(data))
    response = urllib2.urlopen(r)
    r = response.read()
    final = json.loads(r)
    result = final['results'][0]
    face_id = result['face_image_id']  ## get the face_id for the image search
    data = {
        "retrieval": {
            "face_image_id": face_id,
            "repository_ids": [id],
            "threshold": 38, 
         },
        "fields": [ "face_image_id", "repository_id", "timestamp", "name", "person_id" ],
        "condition": {
        },
        "order": { "similarity": -1 }, 
        "start": 0, "limit": 1 
    }
    r = urllib2.Request("http://127.0.0.1:9200/face/v1/framework/face/retrieval",headers={"session_id": gid.get_id()},data=json.dumps(data))
    response = urllib2.urlopen(r)
    r = response.read()
    final = json.loads(r)
    result = final['results'][0]
    return result['face_image_id']



def find_image():
    data = {
        "fields": [ "face_image_id", "repository_id", "timestamp", "face_image_uri", "is_hit", "camera_id" ],
        "condition": {
            "repository_id": { "$in": [15] },
        },
        "order": { "timestamp": -1 },
        "start": 0, "limit": 10
    }
    r = urllib2.Request("http://127.0.0.1:9200/face/v1/framework/face/query", 
    headers={"session_id":gid.get_id()}, data=json.dumps(data))
    response = urllib2.urlopen(r)
    r = response.read()
    final = json.loads(r)