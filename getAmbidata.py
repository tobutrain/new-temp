import json
import requests
with open('src/ambientKey.json') as ambientURLJs:
    ambientURL = json.load(ambientURLJs)['AmbiURL']

def getAmbientTemp(getURL):
    getData = json.loads(requests.get(str(getURL)).text)[0]['d1']
    return getData

def getAmbientTime(getURL):
    getData = json.loads(requests.get(str(getURL)).text)[0]['created']
    return getData

tempData = []
for i in range(len(ambientURL)):
    tempData.append(getAmbientTemp(ambientURL[i]))

timeData = []
for i in range(len(ambientURL)):
    timeData.append(getAmbientTime(ambientURL[i]))

for i in range(len(tempData)):
    print("temp: "+str(tempData[i])+" time: "+str(timeData[i]))