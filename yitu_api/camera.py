import requests
import hashlib
import json
import urllib2
import get_session_id as gid

def add_camera():
	data = {"name": "camera_01", "url":  "rtsp://admin:123456@192.168.1.120"}

	r = urllib2.Request("http://127.0.0.1:9900/face/v1/framework/face_video/camera", 
	    headers={"session_id":gid.get_id()},   data=json.dumps(data))
	#print(r.text())
	response = urllib2.urlopen(r)
	r = response.read()
	final = json.loads(r)
	print final


def change_camera():
	data = {"id": 2, "enabled":  1}	
	r = urllib2.Request("http://127.0.0.1:9900/face/v1/framework/face_video/camera", 
	headers={"session_id":gid.get_id()},   data=json.dumps(data))
	r.get_method = lambda: 'PUT'
	response = urllib2.urlopen(r)
	r = response.read()
	final = json.loads(r)

def search_camera():
	r = urllib2.Request("http://127.0.0.1:9900/face/v1/framework/face_video/camera", 
	headers={"session_id":gid.get_id()})
	#print(r.text())
	response = urllib2.urlopen(r)
	r = response.read()
	final = json.loads(r)

def delete_camera():
	r = urllib2.Request("http://127.0.0.1:9900/face/v1/framework/face_video/camera?id=1", 
	headers={"session_id":gid.get_id()})
	r.get_method = lambda: 'DELETE'
	response = urllib2.urlopen(r)
	r = response.read()
	final = json.loads(r)

def add_connect():
	data = {"camera_id": 2, "repository_id":  14, "threshold": 20}	
	r = urllib2.Request("http://127.0.0.1:9900/face/v1/framework/face_video/surveillance", 
	headers={"session_id":gid.get_id()}, data=json.dumps(data))
	#print(r.text())
	response = urllib2.urlopen(r)
	r = response.read()
	final = json.loads(r)

def get_connect():
	r = urllib2.Request("http://127.0.0.1:9900/face/v1/framework/face_video/surveillance", 
	headers={"session_id":gid.get_id()})
	#print(r.text())
	response = urllib2.urlopen(r)
	r = response.read()
	final = json.loads(r)

def change_connect():
	data = {"id": 0, "threshold": 39, "max_time_span":  5, "min_time_span" : 4}
	r = urllib2.Request("http://127.0.0.1:9900/face/v1/framework/face_video/surveillance", 
	headers={"session_id":gid.get_id()}, data=json.dumps(data))
	r.get_method = lambda: 'PUT'
	response = urllib2.urlopen(r)
	r = response.read()
	final = json.loads(r)


