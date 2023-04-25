#Program to check given year is leap year or not
n=int(input("Enter a year: "))
if((n%100==0)and(n%400==0)) or ((n%4==0)and(n%100!=0)):
    print("Leap year!!")
else:
    print("Not a leap year!!")