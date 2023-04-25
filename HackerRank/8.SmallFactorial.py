def fact(x):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    for i in range(1,n+1):
        print(fact[i])

n=int(input("Enter total no. of testcases:- "))
while(n>0):
    x=int(input("Enter the element to find factorial:- "))
    fact(x)
    n=n-1