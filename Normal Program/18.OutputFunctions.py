'''OUTPUT STATEMENTS:-->
------------------------
print("control string/format specifier",(variable_name))
--------------------------------------------------------
1. print("Control string") --> ex. print("GLA") --> GLA
2. print(object) --> x=10 print(x) --> 10
3. print("Control string",object) --> print("GLA",x)  --> GLA 1
4. print("Control string/format specifier" % (variable_name))
    ex. x=1 y=2
        print("The value of x is %d and value of y is %d" % (x,y))
5. print("Control string with format" .format(variable_name))
    ex. print("The value of x is {0} and value of y is {1}" .format (x,y))
        print("The value of x is {a} and value of y is {b}" .format (a=x,b=y))
'''
x = 10 
y = 20
print("The value of x is %d and value of y is %d" % (x,y))
print("The value of x is {0} and value of y is {1}" .format (x,y))
print("The value of x is {a} and value of y is {b}" .format (a=x,b=y))