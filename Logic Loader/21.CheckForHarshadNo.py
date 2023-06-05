#If a no. is divisible by the sum of its digits, then it will be known as HARSHAD NO.
n=int(input("Enter a no.:  "))
rem=sum=0
m=n
while(m>0):
    rem=m%10
    sum=sum+rem
    m=m//10
if(n%sum==0):
    print(str(n)+" is a Harshad no.")
else:
    print(str(n)+" is not a Harshad no.")