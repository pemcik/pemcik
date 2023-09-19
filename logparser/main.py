import json
import re
from datetime import datetime
file_name = "/var/log/dpkg.log"
file = open(file_name, "r")
data = []
order = ["date", "time", "triger", "task", "package", "version"]

for line in file.readlines():
    details = line.split(" ")
    details = [x.strip() for x in details]
    structure = {key:value for key, value in zip(order, details)}
    data.append(structure)
save_file = open("/home/parrot/pysec2023/1.json", "w")
json.dump(data,save_file,indent = 6)
save_file.close()
with open("/home/parrot/pysec2023/1.json", "r") as f:
  data1 = json.load(f)
  date = data1["date"]
  for date in data1:
     print(date)

#print(data1[date][0][time][0][package] + ":")

    #for entry in data:
        #print(json.dumps(entry, indent = 6))

#print(data)
