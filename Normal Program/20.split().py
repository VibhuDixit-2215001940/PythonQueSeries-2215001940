'''split():- 
-------------
It is used to taking more than one value from the user.
By default value of it is space.
If we are using split() than the value must be in single line having spaces separated.
We can take value one by one by changing default value by our choice.
'''
#DEFAULT SEPARATION
x,y = input("Enter your name:- ").split()
print("Value of x is:- ",x)
print("Value of y is:- ",y)
#SEPARATION BY CHOICE
x,y = input("Enter your name:- ").split(',')
print("Value of x is:- ",x)
print("Value of y is:- ",y)