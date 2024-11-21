with open("thickk.txt","r",encoding="utf-8") as file:
    data1 = file.read()

print(data1)
print("")
print("File name: ",file.name)

lines=data1.split()

symbols=len(data1)
print("Number of symbols and words",symbols)

count_word=len(lines)
print("Number of words",count_word)



file=open("thickk.txt",encoding="utf-8")
lines = file.readlines()
line_count=len(lines)
print("Number of lines",line_count)


file=open("thickk.txt",encoding="utf-8")
print("First 10 symbols: ",file.read(10))

file=open("thickk.txt",encoding="utf-8")
data1 = file.read()[0]
print("First symbol: ",data1)

file=open("thickk.txt",encoding="utf-8")
data1 = file.read()[-1]
print("Last symbol:", data1)

def funk():
    file=open("thickk.txt",encoding="utf-8")
    lines = file.readlines()
    print("First line of this absolute banger: ",lines[0])
    
funk()