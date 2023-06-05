#PERFECT NO.--> A no. whoes factors sum is equal to its digit.
n=int(input("Enter a no.: "))
sum=0
for i in range(1,n+1):
    if (i%n==0):
        sum+=i
if(n==sum):
    print("PERFECT NO.!!")
else:
    print("NOT A PERFECT NO.!!")