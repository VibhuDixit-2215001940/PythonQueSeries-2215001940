#Taking Nested Tuple
r=int(input("Enter the no. of rows: "))
c=int(input("Enter the no. of columns: "))
x=()
for i in range(r):
	y=()
	for j in range(c):
		z=int(input("Enter value: "))
		y=y+z,
	x=x+y,
print()
print(x)
