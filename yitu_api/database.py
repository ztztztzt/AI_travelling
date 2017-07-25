import requests
import hashlib
import json
import urllib2
import get_session_id as gid



def construct_database():
	data = {"name": "test_facerecog_pic", "type":  0, "comment" : "The database for face recognition algorithm",
			"id" : 18}

	r = urllib2.Request("http://127.0.0.1:9900/face/v1/framework/face_image/repository", 
	    headers={"session_id":gid.get_id()},   data=json.dumps(data))
	#print(r.text())
	response = urllib2.urlopen(r)
	r = response.read()
	final = json.loads(r)
	print final

def delete_database(): #change id number
		r = urllib2.Request("http://127.0.0.1:9900/face/v1/framework/face_image/repository?id=16", 
		    headers={"session_id":gid.get_id()})
		r.get_method = lambda: 'DELETE'
		response = urllib2.urlopen(r)
		r = response.read()
		final = json.loads(r)		
		print final

def search_database():

	r = urllib2.Request("http://127.0.0.1:9900/face/v1/framework/face_image/repository", 
	    headers={"session_id":gid.get_id()})
	#print(r.text())
	response = urllib2.urlopen(r)
	r = response.read()
	final = json.loads(r)
	print final

def change_database():
	data = {"id": 8, "name" : "try1"}
	r = urllib2.Request("http://127.0.0.1:9900/face/v1/framework/face_image/repository", 
	    headers={"session_id":gid.get_id()}, data=json.dumps(data))
	r.get_method = lambda: 'PUT'
	response = urllib2.urlopen(r)
	r = response.read()
	final = json.loads(r)
	print final




