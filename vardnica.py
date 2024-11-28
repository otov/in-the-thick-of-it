tulkojums={"House":"Māja","City":"Pilsēta","Road":"Ceļš"}
print(tulkojums)
print(tulkojums["House"])

print(len(tulkojums))

sekmes={"Nauris":{"sem1":5,"sem2":4},
        "Kristaps":{"sem1":3 , "sem2": 4},
        "Dāvis":{"sem1": 6, "sem2": 1}}

print(sekmes)
skm=sekmes["Nauris"]
skm1=skm["sem2"]
print(skm)
print("2. semestris: ",skm1)

sekmes["Koļa"]={"sem1":7, "sem2": 6}
print(sekmes)

print("Sekmju saraksta skolenu skaits: ",len(sekmes))

#vardinas papildinasana
gramata={"Nosaukums":"The war of the worlds", "Autors":"Herbert George Wells"}
print(gramata)
papildus_dati={"Gads":1898, "Žanrs": "Zinātniskās fantastikas romāns"}
gramata.update(papildus_dati)
print(gramata)


atzimes={10:"Izcili", 9:"Teicami", 8:"Ļoti labi", 7:"Labi",6:"Gandrīz labi", 5:"Viduvēji", 4:"Gandrīz viduvēji", 3:"Vāji", 2:"Vāji",1:"Ļoti vāji"}
print(atzimes)

while True:
    try:
        atz=int(input("Ievadīt skaitli 1-10: "))
        if 1<= atz <=10:
            break
        else:
            print("Ievadīts nederīgs skaitlis")

    except ValueError:
        print("Ievadītam skaitlim ir jābūt veselam!")




skaidrojums=atzimes[atz]
print("Vārdiskais skaidrojums atzīmei:",atz, "ir",skaidrojums)