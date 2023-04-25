#ArmstrongOrNot
n=int(input("Enter the no.:- "))
m=n
result=0
order=len(str(n))
while(m!=0):
    last_digit=n%10
    result=result+last_digit**order
    n=n//10
    m=m-1
if(result==m):
    print("Armstrong!!")
else:
    print("Not a armstrong!!")