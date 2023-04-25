n=int(input())      #No. of testcases
l=[]        #Defining a list
while(n>0):
    x=int(input())      #Taking elements 
    l.append(x)
    n=n-1
l.sort()                #Ascending order
for i in l:
    print("Ascending order:- ",i)