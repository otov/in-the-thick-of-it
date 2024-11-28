alfabets=["A","Ā","B","C","Č","D","E","Ē","F","G","Ģ","H","I","Ī","J","K","Ķ","L","Ļ","M","N","Ņ","O","P","R","S","Š","T","U","Ū","V","Z","Ž"]
vardi={burti: None for burti in alfabets}

def valid(vards):
    return vards[0].isupper() and vards.isalpha()

def pievienot(vards):
    if not valid(vards):
        print("Ievadīts nederīgs vārds! Lūdzu ievadiet citu vārdu!")
        return
    
    pirmais_burts = vards[0].upper()

    if pirmais_burts in vardi:
        if vardi[pirmais_burts] is None:
            vardi[pirmais_burts]=vards
            print("Pievienoju vardu",vards," vietā ",pirmais_burts)
        else:
            print("Vārds vietā",pirmais_burts," jau ir aizņemts. Apmainu vārdu ",vardi[pirmais_burts],"ar",vards)
            vardi[pirmais_burts]=vards
    else:
        print("Ievadīts nepareizs pirmais burts. ludzu ievadiet citu!")

def izvade():
    print("\nAlfabeta vārdi: ")
    for burti, vardss in vardi.items():
        if vardss:
            print(f"{burti}: {vardss}")
        else:
            print(f"{burti}: nav vārda.")

def aizpildits():
    return all(vardss is not None for vardss in vardi.values())

def galvena_programma():
    vaardi=["Ainaži","Salacgrīva","Dobele","Sabile","Kuldīga","Ventsplils","Rīga","Daugavpils","Zilupe","Vangaži","Cēsis","Alūksne","Valmiera","Bauska","Jelgava","Saldus","Talsi","Jēkabpils","Liepāja","Kolka","Ādaži","Ērgļi","Grobiņa","Olaine","Engure","Nereta","Pāvilosta","Iecava","Ķegums"]

    for vardss in vaardi:
        pievienot(vardss)
        izvade()

        if aizpildits():
            print("\n Alfabēts ir pilnīgi aizpildīts")
            break

galvena_programma()