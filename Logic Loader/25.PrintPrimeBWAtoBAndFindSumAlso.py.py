l = int(input ("Please, Enter the Lowest Range Value: "))  
u = int(input ("Please, Enter the Upper Range Value: "))  
  
print ("The Prime Numbers in the range are: ")  
sum=0
for number in range (l, u + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print(number)
            sum+=number
print("The sum of prime no. b/w range is: ",sum)