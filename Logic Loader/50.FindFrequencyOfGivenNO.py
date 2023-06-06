from numpy import *
l=list(map(int,input("Enter an array: ").split()))
n=array(l)
m=int(input("Enter a no. to find its freq. "))
count=0
for i in n:
    if i==m:
        count+=1
print(f"The no. {m} occurs {count} times!!")