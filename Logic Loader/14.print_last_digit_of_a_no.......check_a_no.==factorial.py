n=int(input("Enter a no.: "))       #123
n=str(n)                            #"123"
m=list(map(int,n))                  #[1, 2, 3]
print(f"Last digit of {n} is: ",m[-1])#3