D={}
print(D)

List=[["a",1],["b",2],["c",3],["d",4],["a",5],["c",8],["a",2]]

for i in range(len(List)):
    if List[i][0] in D:
        D[List[i][0]].append(List[i][1])

    else:
        D[List[i][0]]=[]
        D[List[i][0]].append(List[i][1])

print(D)
