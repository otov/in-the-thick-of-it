import json

dati = {
    "persona":{
        "vārds":"Raimonds",
        "vecums":22,
        "pilseta":"Valmiera",
        "hobijs":["basketbols","video speeles"],   
    },
    "uznemums":{
        "nosaukums":"SIA Apik",
        "amats":"klientu support",
        "darbinieki":32
    }
}

json_datne = json.dumps(dati,ensure_ascii=False, indent = 2)
print(json_datne)

with open("raimonds.json","w",encoding="utf-8")as file:
    file.write(json_datne)