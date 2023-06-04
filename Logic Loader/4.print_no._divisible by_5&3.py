n=int(input("Enter a range to find even no.: "))
print("Even no. b/w range are: ")
for i in range(n+1):
    if i % 5==0 and i % 3==0:
            print(i)