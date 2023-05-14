#a+ --> apend a new file and read without removing existing file
f=open("abc.txt","a+")
n=input("Enter a new string: ")
f.write(n)
f.seek(0)           #To move the cursor at the start to read new string
x=f.read()
print(x)        #Vibhu dixitPari dixit
f.close()