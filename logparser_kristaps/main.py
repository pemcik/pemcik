from libs.AuthLogParser import AuthLogParser
from libs.SysLogParser import SysLogParser
from datetime import datetime
import time


authLogParser = AuthLogParser()
authLogParser.info()
authEvents = authLogParser.readFile()


sysLogParser = SysLogParser()
sysLogEvents = sysLogParser.readFile()


commonLog = authEvents + sysLogEvents


sortedLog = sorted(commonLog, key=lambda d: d['date'])
for event in sortedLog:
    event['date'] = datetime.utcfromtimestamp(event['date']).strftime("%Y %b %d %H:%M:%S")
    # print(event)


mySet = set()
myList = []

for event in sortedLog:
    mySet.add(event['event'])
    myList.append(event['event'])


st = datetime.now()
if 'pam_unix(cron:session): session closed for user root' in mySet:
    print('found event in set')
et = datetime.now()

print("execution time in set of size {} :".format(len(mySet)), (et-st).total_seconds()* 10**3)

st = datetime.now()
if 'pam_unix(cron:session): session closed for user root' in myList:
    print('found event in list')
et = datetime.now()

print("execution time in a list of size {} :".format(len(myList)), (et-st).total_seconds()* 10**3)
