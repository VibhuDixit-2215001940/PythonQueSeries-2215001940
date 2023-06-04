n=int(input("Enter a no: "))
print(f"Factors of {n} are: ")
for i in range(1,n):
    if n % i == 0:
        print(i)