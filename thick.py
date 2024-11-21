with open("Masinmacisanas.txt","r",encoding="utf-8") as file:
    data = file.read()
#print(data)

word_count={}
lines=data.split()#sadala tekstu vardos
print(lines)#izvada sadalitu tekstu

print("")

for word in lines:
    if len(word) >=4:
        if word in word_count:
            word_count[word]+=1
        else:
            word_count[word]=1

print(word_count)

top=sorted(word_count.items(),key=lambda x: x[1],reverse=True)[:5]

for word, count in top:
    print(word,count)