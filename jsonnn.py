import json

with open ("Jsonn.json", "r",encoding="utf-8-sig") as file:
    data=json.load(file)
    print(data)
print("datnes nosaukums ir: ",file.name)