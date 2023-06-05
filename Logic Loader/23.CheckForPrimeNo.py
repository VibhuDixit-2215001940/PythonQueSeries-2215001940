n=int(input("Enter a no: "))
count=0
for i in range(1,n+1):
    if(n%i==0):
        count+=1
if(count==2):
    print("PRIME NO.!!")
else:
    print("NOT A PRIME NO.!!")