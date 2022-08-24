import json
import requests
from datetime import datetime

with open('src/ambientKey.json') as ambientURLJs:
    ambientURL = json.load(ambientURLJs)['AmbiURL']

def getAmbientTemp(getURL):
    getData = json.loads(requests.get(str(getURL)).text)[0]['d1']
    return getData

def getAmbientTime(getURL):
    getData =str(datetime.strptime(json.loads(requests.get(str(getURL)).text)[0]['created'] + '+0000', '%Y-%m-%dT%H:%M:%S.%fZ%z').astimezone().replace(microsecond=0)).replace('+09:00','').replace('-','/')
    return getData

timeData = []
tempData = []
for i in range(len(ambientURL)):
    tempData.append(getAmbientTemp(ambientURL[i]))
    timeData.append(getAmbientTime(ambientURL[i]))

timeTemp = []
for i in range(len(timeData)):
    timeTemp.append({"No":i+1,"temp":tempData[i], "time":timeData[i]})
with open('src/timeTemp.json', 'w') as outputFile:
    json.dump({"timeTemp":timeTemp}, outputFile)