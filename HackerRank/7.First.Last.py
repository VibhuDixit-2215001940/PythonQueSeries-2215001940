def check(x):
    y=str(x)
    c=(int(y[0])+int(y[-1]))
    return c

n=int(input("Enter total no. of testcases:- "))
while(n>0):
    x=int(input("Enter the outcomes: "))
    check(x)
    n=n-1