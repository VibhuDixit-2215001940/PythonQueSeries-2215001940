def is_prime(n):
   for i in range(2, n):
      if n % i == 0:
         return False
   return True

def generate_twins(n, m):
   for i in range(n, m):
      j = i + 2
      if(is_prime(i) and is_prime(j)):
         print("{:d} and {:d}".format(i, j))

n=int(input("Enter the first limit: "))
m=int(input("Enter the first limit: "))
generate_twins(n, m)            #3 and 5
                                #5 and 7