#Printing Boundaries elements 
r=int(input("Enter the no. of rows: "))
c=int(input("Enter the no. of columns: "))
x=[]
for i in range(r):
	y=[]
	for j in range(c):
		y.append(input("Enter the value: "))
	x.append(y)
for i in range(r):
	for j in range(c):
		if(i==0 or i==r-1 or j==0 or j==r-1):
			print(x[i][j],end=' ')
		else:
			print( " ",end=' ')
	print()