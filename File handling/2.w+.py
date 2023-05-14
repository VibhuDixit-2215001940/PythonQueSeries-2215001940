#w+ --> write and read by removing existing file
f=open("abc.txt","w+")
n=input("Enter a new string: ")
f.write(n)
f.seek(0)           #To move the cursor at the start to read new string
x=f.read()
print(x)        #Pari dixit
f.close()