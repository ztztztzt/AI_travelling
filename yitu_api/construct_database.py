import requests
import hashlib
import json
import urllib2
import get_session_id as gid


if __name__ == "__main__":


    data = {"name": "VE450_Team28", "type":  1, "comment" : "This is the database from Shanghai Jiaotong University Joint Institute, Team 28. Photos from travelling website"}

    r = urllib2.Request("http://127.0.0.1:9900/face/v1/framework/face_image/repository", 
        headers={"session_id":gid.get_id()},   data=json.dumps(data))
    #print(r.text())
    response = urllib2.urlopen(r)
    r = response.read()
    final = json.loads(r)
    print final