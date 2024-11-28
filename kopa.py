#izveido kopu
grozs={"Udens","Maize","Piens","Kartupeļi"}
kopa=set(grozs)
print(kopa)

#izveido ciparu kopu
cipari={3,1,5,9,9,5,4,1,7,2}
print(cipari)
#kopa1=set(cipari)
#print(kopa1)

#pievieno elementu kopai
auto={"BMW","Opel","Mercedes"}
auto.add("Audi")#pievieno elementu
print(auto)

#kopai pievieno velvienu
auto1={"BMW","Audi","Mercedes"}
auto1.update({"Ford","Dodge"})
print(auto1)

#apvieno divas kopas
cilveki1={"Juris","Mareks"}
cilveki2={"Raimonds","Jāzeps"}
dzeki=cilveki1|cilveki2
print(dzeki)

#noņemt konkrētu elementu
auto3={"BMW","Audi","Mercedes"}
auto3.discard("Audi")
print(auto3)

#izveido kopu šķēlumu
parask={2,4,6,8,10,12,14,16,18,20,22,24,26,28,30}
dalartris={3,6,9,12,15,18,21,24,27,30}
skelums=parask.intersection(dalartris)
print(skelums)