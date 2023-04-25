#PERCENTAGE AND GRADE OF FIVE SUBJECTS
a=int(input("Enter the marks of Physics:- "))
b=int(input("Enter the marks of Chemistry:- "))
c=int(input("Enter the marks of Biology:- "))
d=int(input("Enter the marks of Computer:- "))
e=int(input("Enter the marks of Mathematics:- "))
total=a+b+c+d+e
per=(total/5)
if per>=90:
    grade='A'
elif per>=80:
    grade='B'
elif per>=70:
    grade='C'
elif per>=60:
    grade='D'
elif per>=50:
    grade='E'
elif per>=30:
    grade='F'
print("Total marks are: ",total)
print("Percentage are: ",per)
print("Grade: ",grade)