#CHAR. IS ALPHABET, DIGIT OR SPECIAL CHARACTER
ch=input("Enter a character: ")
if ch>='a' and ch<='z':
    print("Lowercase alphabet!!")
elif ch>='A' and ch<='Z':
    print("Uppercase Alphabet!!")
elif  ch.isdigit():
    print("Digit!!")
else:
    print("Special Character!!")