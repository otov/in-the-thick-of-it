alfabets=["A","Ā","B","C","Č","D","E","Ē","F","G","Ģ","H","I","Ī","J","K","L","Ļ","M","N","Ņ","O","P","R","S","Š","T","U","Ū","V","Z","Ž"]
vardi={burti: None for burti in alfabets}

def valid(vards):
    return vards[0].isupper() and vards.isalpha()

def pievienot(vards):
    if not valid(vards):
        print("Ievadīts nederīgs vārds! Lūdzu ievadiet citu vārdu!")
        return
    
    