#Write a python script to demonstrate ATM machine logic, in which user enters 
#the amount and you have to print no. of notes of 2000,500,200,100.
amount = int(input("Enter the amount: "))
a = amount // 2000      #No. Of 200 Notes
b = amount % 2000       #Rest Money

c = b // 500
d = b % 500

e = d // 200
f = d % 200

g = f // 100
h = f % 100

print("2000-",a)
print("500-",c)
print("200-",e)
print("100-",g)
