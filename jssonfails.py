import json

with open("datii.json","r",encoding="utf-8-sig") as file:
    data=json.load(file)
    print(data)
print("Faila nosaukums: ",file.name)