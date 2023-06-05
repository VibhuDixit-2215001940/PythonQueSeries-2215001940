from numpy import *
n=array([1,2,3,4,5,6,7,8,9,15])
count=0
for i in n:
    if i%2==0:
        count+=1
print("No. of even elements are: ",count)