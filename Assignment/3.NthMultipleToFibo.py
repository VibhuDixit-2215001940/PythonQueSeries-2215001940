#Nth MULTIPLE OF A NO. TO FIBONACCI SERIES
z=0
x=0
y=1
n=int(input("Enter the limit: "))
m=int(input("Enter the no. to multiply: "))
while(n>0):
    print(z*m)
    x=y
    y=z
    z=x+y
    n=n-1
