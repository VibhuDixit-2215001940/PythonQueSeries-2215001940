from numpy import *
n=array([1,2,3,4,5,6,7,8,9,15])
sum=0
l=[]
for i in n:
    if i%2==0:
        l.append(i)
for i in l:
    sum+=i
print("Sum of all even elements are: ",sum)