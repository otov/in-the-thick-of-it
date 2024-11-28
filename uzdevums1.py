saraksts1=["Bmw","Audi","Mercedes"]
print(saraksts1)
print("Garums: ",len(saraksts1))

saraksts1.append("Seat")
print(saraksts1)

saraksts1.pop(1)
print(saraksts1)

saraksts2=["Latvija","Lietuva","Igaunija","Somija","Zviedrija","Norvēģija"]
print(saraksts2)
for i in reversed(range(0,6)):#cikls, kas apgriež otraadak sarkstu
    print(saraksts2[i])#izdrukaa 