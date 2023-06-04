n=int(input("Enter a no: "))
m=str(n)
print(m[::-1])
if m==m[::-1]:
    print("No. is Palindrome!!")
else:
    print("Not a palindrome no.!!")