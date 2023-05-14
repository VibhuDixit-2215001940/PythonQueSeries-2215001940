#r+--> reads the file and then write in a existing file
f=open("abc.txt","r+")
x=f.read()
print(x)
n=input("Enter string to add: ")
f.write(n)
f.close()       #f becomes Vibhu dxitkavyansh dixit