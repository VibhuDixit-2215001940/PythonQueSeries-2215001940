import math
def perfect_square(x):
    s=int(math.sqrt(x))
    return s*s==x

n=int(input("Enter the no.:- "))
result1=5*(n*n)+4
result1=5*(n*n)-4

if perfect_square(result1) or perfect_square(result2):
    print(n,"is fibonacci no.")
else:
    print(n,"is not a fibonacci no.")
