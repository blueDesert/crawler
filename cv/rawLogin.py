#!/usr/bin/env python3
import requests
import sys 
import xml.etree.ElementTree as ET
import base64
import json


user = None
pwd = None
service = 'http://<<server>>:81/SearchSvc/CVWebService.svc/'

#1. Login
if len(sys.argv) < 3:
        print ("Server name and username are required arguments")
        sys.exit(0)

server = sys.argv[1]
service = service.replace("<<server>>", server)
user = sys.argv[2]

loginReq = '<DM2ContentIndexing_CheckCredentialReq mode="Webconsole" username="<<username>>" password="<<password>>" />'

#add auth with json format
loginReq_json = '''
{
"username":"admin",
"password":"MXFhekBXU1g="
}
'''

headers = {'Accept':'application/json','Content-type':'application/json'}


if user is None:
        print ("Username is required")
        sys.exit(0)
else:
        loginReq = loginReq.replace("<<username>>", user)

if len(sys.argv) > 3:
        pwd = sys.argv[3];


if pwd is None:
        loginReq = loginReq.replace("<<password>>", "")
else:
        pwd = bytes(pwd, encoding='utf8')
        pwd = str(base64.b64encode(pwd), encoding='utf-8')
        loginReq = loginReq.replace("<<password>>", pwd)

r = requests.post(service + 'Login', data=loginReq)
r_json = requests.post(service + 'Login', data=loginReq_json , headers = headers)
#print(r_json.text)
print('===============token==============')
#print(json.loads(r_json.text)['token'])
print('=====================below as using XML=====================')
#print(service+'Login')
#print(loginReq)
token = None

if r.status_code == 200:
        root = ET.fromstring(r.text)
        if 'token' in root.attrib:
                token = root.attrib['token']
                #print(token)
                print ("Login Successful")
        else:
                print ("Login Failed")
                sys.exit(0)
else:
        print ('there was an error logging in')

#Add header using json
#headers = {'Cookie2': token,'Content-type':'application/json'}
headers = {'Authtoken': token,'Content-type':'application/json','Accept':'application/json'}
#headers = {'Authtoken': token,'Content-type':'application/json'}

#get client information
#clientPropsReq = service + 'Subclient?clientId=2'
#clientPropsReq = service + 'Subclient/2/action/backup?backupLevel=Incremental'
clientPropsReq = service + 'Subclient/7/action/backup'
print(clientPropsReq)

#get response using get
r = requests.post(clientPropsReq, headers=headers)
clientResp = r.text
print(clientResp)

