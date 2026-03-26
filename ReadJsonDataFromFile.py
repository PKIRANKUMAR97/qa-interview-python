import json
data ={'name': 'Kiran', 'skills': ['Python', 'Selenium', 'API', 'SQL']}
with open(r"E:\Pavan_Trainings\Data_json.json","w") as file:
    json.dump(data,file,indent=4)

print("write data --- ",data)

with open(r"E:\Pavan_Trainings\Data_json.json","r") as file :
    data = json.load(file)

print("read data---",data)