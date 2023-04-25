#Python progrm to change first and last element of a lis
l=list(map(int,input("Enter a list: ").split()))
print("Entered list: ",l)
l[0],l[-1]=l[-1],l[0]
print("Modified list|: ",l)