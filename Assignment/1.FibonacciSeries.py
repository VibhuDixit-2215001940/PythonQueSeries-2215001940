#FIBONACCI SERIES
z=0
x=0
y=1
n=int(input("Enter the limit: "))
while(n>0):
    print(z)
    x=y
    y=z
    z=x+y
    n=n-1