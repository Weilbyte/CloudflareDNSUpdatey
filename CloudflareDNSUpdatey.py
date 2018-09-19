
import sys
import argparse
import json
import requests

#Parse arguments
aparser = argparse.ArgumentParser()
aparser.add_argument('-email', help="Email to the Cloudflare account", required=True)
aparser.add_argument('-token', help="The API key", required=True)
aparser.add_argument('-zone', help="Targeted zone", required=True)
aparser.add_argument('-record', help="Record to update", required=True)
arguments = vars(aparser.parse_args())

cfUrl = "https://api.cloudflare.com/client/v4/"
rhead = {'X-Auth-Key': arguments['token'], 'X-Auth-Email': arguments['email'], 'Content-type': 'application/json'}
#Get our iP
try:
    ip = requests.get(r'http://jsonip.com').json()['ip']
except: 
    print("Unable to retrieve external IP address!")
print("External IP address is " + ip)

#Get zone ID
r=requests.get(cfUrl + "zones?name=" + arguments['zone'], headers=rhead)
for res in r.json()['result']:
    zoneID = res['id']

#Get records details and compare IPs
r=requests.get(cfUrl + "zones/" + zoneID + "/dns_records?name=" + arguments['record'], headers=rhead)
for res in r.json()['result']:
    recIP = res['content']
    recID = res['id']
    recType = res['type']
    recName = res['name']

if recIP != ip:
    print("Updating record..")
    udata = json.dumps({'type': recType, 'name': recName, 'content': ip})
    r = requests.put(cfUrl + "zones/" + zoneID + "/dns_records/" + recID, data=udata, headers=rhead)
    print(r.json())

if recIP == ip:
    print("Record already up to date")
    





