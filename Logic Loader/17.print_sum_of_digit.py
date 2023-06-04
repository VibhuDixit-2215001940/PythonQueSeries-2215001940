n=int(input("Enter a no.: "))
m=list(map(int,str(n)))
sum=0
for i in m:
    sum=sum+i
print(f"Sum of digit of {n} is: ",sum)