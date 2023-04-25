def swap(x,y):
    x=x^y
    y=x^y
    x=x^y
    return x,y

n=int(input("Enter the first no.: "))
m=int(input("Enter the second no.: "))
print("Before swapping: ",(n,m))
print("After swapping: ",swap(n,m))
