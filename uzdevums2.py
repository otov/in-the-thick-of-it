saraksts= list(range(1,11))
print(saraksts)

kvadrati=[x**3 for x in saraksts]
print(kvadrati)

kop_saraksts=saraksts+kvadrati
print(kop_saraksts)

mazakais=min(saraksts)
print(mazakais)
lielakais=max(saraksts)
print(lielakais)

summa=sum(saraksts)
print(summa)

print(sum(saraksts))

pilsetas=["Ventspils","Liepāja","Talsi","Saldus","Kuldīga"]
print(pilsetas)
garakais=max(pilsetas, key=len)
print(garakais)

isakais=min(pilsetas, key=len)
print(isakais)