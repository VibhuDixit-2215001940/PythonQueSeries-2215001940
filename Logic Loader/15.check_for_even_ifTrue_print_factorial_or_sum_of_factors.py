def fact(n):
    mul=1
    for i in range(1,n+1):
        mul=mul*i
    print(f"Factorial of {n} is: ",mul)

n=int(input("Enter a no.: "))
if n % 2 == 0:
    print("No. is even: ")
    fact(n)
else: 
    print("No. is odd: ")
    sum=0
    for i in range(1,n+1):
        if n % i == 0:
            sum=sum+i
    print(f"Sum of all factors of {n} is: ",sum)