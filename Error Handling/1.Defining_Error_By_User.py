try:
    n=int(input("Enter a no.: "))
    a=100
    c=a/n
    print(c)
except ZeroDivisionError:
    print("Error")
finally:
    print("Thanks")