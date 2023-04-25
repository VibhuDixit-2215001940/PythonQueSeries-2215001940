def swap(n):
    num=""
    for i in n:
        if i .isupper==True:
            num=num+(i.lower())
        else: 
            num=num+(i.upper())
    return num
n=input()
result=swap(n)
print(result)

