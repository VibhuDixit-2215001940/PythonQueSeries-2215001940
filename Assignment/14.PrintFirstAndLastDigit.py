#PRINTING FIRST AND LAST DIGIT OF A NO.
n=input("Enter a no.: ")
if (n.isnumeric):
    for i in range(len(n)):
        if i==0:
            print(f"First Digit Is: {n[0]}")
        elif i==len(n)-1:
            print(f"Last Digit Is: {n[-1]}")
else:
    print("Please enter a valid no......Please Try Again!!")
