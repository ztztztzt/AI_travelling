import requests
import hashlib
import json
import urllib2


def get_id():   

    data = {"name": "admin", "password":  "21232f297a57a5a743894a0e4a801fc3" }

    r = urllib2.Request("http://127.0.0.1:7500/resource_manager/user/login", 
        headers={"Content-Type":"application/json"},   data=json.dumps(data))
    #print(r.text())
    response = urllib2.urlopen(r)
    r = response.read()
    final = json.loads(r)
    return final["session_id"]


    