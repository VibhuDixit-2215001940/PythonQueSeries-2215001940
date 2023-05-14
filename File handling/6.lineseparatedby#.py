f=open("abc.txt","r")
x=f.read()
l=[]
for i in x:
    for j in i:
        if j=='#':
            l.append(i)

print(l)
f.close()