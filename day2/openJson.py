import json

f = open('parameter.json')

data = json.load(f)

print("Subject", data["Subject"])
print("file", data["File"])
for i in data['FIle']:
    for j in i:
        print("key is :", j, " value is :", i.gett(j))

f.close()