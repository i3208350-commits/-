import json
profile = {"name": "Dana", "grades": [90, 85, 100]}
fili="profile.json"

with open(fili,"w")as file:
    json.dump(profile,file)
with open(fili,"r") as file:
    k=json.load(file)
    print(k)
