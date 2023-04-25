'''l=list(map(int,input("Enter a list: ").split()))
ele=int(input("Enter an element: "))
print(l.count(ele))'''


z='''l=list(map(int,input("Enter a list: ").split()))
     ele=int(input("Enter an element: "))
    count=0
    for i in l:
        if(i==ele):
        count+=1
    if(count!=0):
        print("Occurence is: ",count)
    else:
        print("Not found!!")'''
exec(z)