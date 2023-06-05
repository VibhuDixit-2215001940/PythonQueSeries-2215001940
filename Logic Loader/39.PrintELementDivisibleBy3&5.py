from numpy import *
n=array([1,2,3,4,5,6,7,8,9,15])
for i in n:
    if i%5==0 and i%3==0:
        print(i)