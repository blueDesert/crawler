#!/usr/bin/env python3
import requests
import sys
import xml.etree.ElementTree as ET
import base64

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
	#encode password in base64 for Python 1 and 2
	#loginReq = loginReq.replace("<<password>>", base64.b64encode(pwd))
	
	#encode password in base64 for Python 3
	pwd = bytes(pwd, encoding='utf8')
	pwd = str(base64.b64encode(pwd), encoding='utf-8')
	loginReq = loginReq.replace("<<password>>", pwd)
	
#Login request built. Send the request now:
r = requests.post(service + 'Login', data=loginReq)
token = None

#Check response code and check if the response has an attribute "token" set
if r.status_code == 200:
	root = ET.fromstring(r.text)
	if 'token' in root.attrib:
		token = root.attrib['token']
		print ("Login Successful")
	else:
		print ("Login Failed")
		sys.exit(0)
else:
	print ('there was an error logging in')

#Login successful.	
#2. Get client props. Client Id is hard coded to 2. 
clientId = "2"
clientPropsReq = service + "client/" + clientId

#build headers with the received token
headers = {'Cookie2': token}
r = requests.get(clientPropsReq, headers=headers)
clientResp = r.text

#Parse response to get client name, host name and client description
client = ET.fromstring(clientResp)

activePhysicalNode = client.findall(".//ActivePhysicalNode")
print ("Client Name: " + activePhysicalNode[0].attrib["clientName"])
print ("Host Name: " + activePhysicalNode[0].attrib["hostName"])

cd = client.findall(".//clientProperties/client")
if 'clientDescription' in cd[0].attrib:
	print ("Client Desc: " + cd[0].attrib["clientDescription"])

clientProps = client.findall(".//clientProps")
if 'JobPriority' in clientProps[0].attrib:
	print ("Job Priority: " + clientProps[0].attrib["JobPriority"])

#3. Set client props
#The following request XML is hard coded here but can be read from a file and appropriate properties set.
updateClientProps = '<App_SetClientPropertiesRequest><clientProperties><clientProps JobPriority="<<jobPriority>>"></clientProps></clientProperties></App_SetClientPropertiesRequest>'
updateClientProps = updateClientProps.replace("<<jobPriority>>", "7")

#Fire the request and print output

r = requests.post(clientPropsReq,data=updateClientProps, headers=headers)
resp = r.text
print (resp)
respRoot = ET.fromstring(resp)
respEle = respRoot.findall(".//response")
errorCode = respEle[0].attrib["errorCode"]

if errorCode == "0":
	print ("Client properties set successfully")
else:
	print ("Client properties could not be set. Error Code: " + errorCode )


