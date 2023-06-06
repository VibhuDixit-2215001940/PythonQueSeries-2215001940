from numpy import *
l=list(map(int,input("Enter an array: ").split()))
n=sorted(l)
m=int(input("Enter the kth smallest element to find: "))
print(f"The {m}th smallest no. is: ",n[m])
