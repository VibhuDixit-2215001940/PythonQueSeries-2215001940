n=int(input("Entera a no.: "))
sum=0
m=n
while m>0:
    a=m%10
    sum=sum+a**len(str(n))
    m=m//10
if n==sum:
    print(n," is a Armstrong no.!!")
else:
    print(n," is not a Armstrong nno.!!")