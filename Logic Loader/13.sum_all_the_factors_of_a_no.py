n=int(input("Enter a no: "))
sum=0
for i in range(1,n):
    if n % i == 0:
        sum=sum+i
print(f"Sum of all factors of {n} is: ",sum)