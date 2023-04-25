n=int(input("Enter no. of students:- "))        #Taking total no. students
std={}              #Defining a set
for i in range(n):      #Loop for n no. of students
    name,*line=input("Enter name & marks:- ").split()   #Taking marks & names
    scores=list(map(float,line))        #Separating  marks
std[name]=scores            #Dictinary formed with key and values
query_name=input("Enter name to find average:- ")   #Taking  student name to find 
output=list(std[query_name])        #Accesing marks of that student
avg=sum(output)/len(output)         #Formula for average
print("The avg is %.2f"%avg)
