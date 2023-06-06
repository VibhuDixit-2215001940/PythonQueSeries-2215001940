from numpy import *
l=list(map(int,input("Enter an array: ").split()))
n=sorted(l)
m=int(input("Enter the kth largest element to find: "))
print(f"The {m}th largest no. is: ",n[-m])
