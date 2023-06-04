a=int(input("Enter first no.: "))
b=int(input("Enter second no.: "))
sum=1
for i in range(a,b+1):
    sum=sum*i
print(f"Multiplication of no. b/w {a} and {b} is ",sum)