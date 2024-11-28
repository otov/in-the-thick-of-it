import json

with open ("jsonn.json", "r",encoding="utf-8") as file:
    data=json.load(file)
    print(data)
print("datnes nosaukums ir: ",file.name)