import json

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
with open('/home/parrot/pysec2023/1.json', 'r') as json_file:
    data = json.load(json_file)
for entry in data:
    print(entry['Date'])
    print(entry['Time'])