from numpy import *
l=list(map(int,input("Enter an array: ").split()))
n=array(l)
m=int(input("Enter an element to search: "))
if m in n:
    print("Founded!!")
else:
    print("Not founded!!")