l=list(input("Enter a list: ").split())
w=input("Enter a word to remove: ")
occur=int(input("Enter the occurence: "))
result=[]
count=0
for i in l:
    if(i==w):
        count+=1
        if(count!=occur):
            result.append(i)
    else:
        result.append(i)
if(count==0):
    print("No element found!!")
else:
    print("List modified is: ",result)