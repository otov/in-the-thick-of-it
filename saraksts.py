#izveidot sarakstu
saraksts=["Bmw","Audi","Mercedes"]
print(saraksts)
print("Saraksta garums: " , len(saraksts)) #noteikt saraksta garumu
print("")

#pielikt elementus saraksta beigās
saraksts.append("Škoda")
print(saraksts)
print("Saraksta garums: " , len(saraksts))
print("")

#ievietot elementu citur
saraksts.insert(0,"Seat")
print(saraksts)
print("Saraksta garums: " , len(saraksts))
print("")

#mainīt elementu secību uz pretējo
saraksts.reverse()
print(saraksts)
print("")

#noņemt elementu pēc secības
saraksts.pop(1)
print(saraksts)
print("")

#noņem specifisku elementu
saraksts.remove("Bmw")
print(saraksts)

#nomanit elementu ar citu elementu
saraksts=["Bmw","Audi","Mercedes"]
saraksts[0]="Opel"
saraksts[1]="Land rover"
saraksts[2]="Ford"
print(saraksts)

sarakstscip=[1,3,5,7,9]
print(type(sarakstscip),'\nx=', sarakstscip)#izdrukā skaitļu rindu kā sarakstu

#divdimensiju masīvs
Divdimensiju_masivs=[[2,4,6,8,10],[1,3,5,7,9],[12,14,16,18,20],[11,13,15,17,19]]
print(Divdimensiju_masivs)