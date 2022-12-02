import json
with open("mock.json","r") as fullfile:
    data=json.load(fullfile)
limdata=[]
for i in data:
    limdata.append(
    {
    "id":i["id"],
    "first_name":i["first_name"],
    "last_name":i["last_name"]
    }
    )
with open("limited.json","w") as limfile:
    json.dump(limdata,limfile,indent=4)

fullfile.close
limfile.close
        