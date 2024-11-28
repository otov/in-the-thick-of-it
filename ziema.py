file=open("Ziema.txt",encoding="utf-8")
#nolasa teksta datni
print(file.read())
print("\n")
file=open("Ziema.txt",encoding="utf-8")
print("Pirmie 11 simboli: ",file.read(11))


file=open("Ziema.txt",encoding="utf-8")
print("Pirmais simbols: ",file.read(1))


file=open("Ziema.txt",encoding="utf-8")
letter=file.read()
print("Pēdējais simbols: ",letter[-1])


with open("Ziema.txt",encoding="utf-8") as file:
    data= file.read()
    lines=data.split()[-1]
print("Pēdējais vārds: ",lines)


number_of_words=0
with open("Ziema.txt",encoding="utf-8") as file:
    data=file.read()
    lines=data.split()
    number_of_words=len(lines)

print("Vārdu skaits: ",number_of_words)


file=open("Ziema.txt",encoding="utf-8")
lines=file.readlines()
line_count=len(lines)
print("Līniju skaits: ",line_count)
    