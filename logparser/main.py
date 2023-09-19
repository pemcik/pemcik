import json
import datetime
file_name = "/var/log/dpkg.log"
file = open(file_name, "r")
data = []
order = ["Date", "Time", "Triger", "Task", "Package", "Version"]

for line in file.readlines():
    details = line.split(" ")
    details = [x.strip() for x in details]
    structure = {key:value for key, value in zip(order, details)}
    data.append(structure)
save_file = open("/home/parrot/pysec2023/1.json", "w")
json.dump(data,save_file,indent = 6)
save_file.close()
fp = open("/home/parrot/pysec2023/1.json")
data = json.load(fp)
#dt = datetime.datetime.now()
#dt_str = dt.strftime("%Y-%m-%d %H:%M:%S")
#json_data = json.dumps(dt_str)
#print(json_data)
#print("Printing incident date, time and package: \n", data)
content = fp.read("Date")
print(content)
#print(data['Date'][0]['Time'][0]['Package'])
