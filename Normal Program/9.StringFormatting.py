#String formating:- It is also known as String Interpolation.
#It is the process of inserting a custom string or variable in a predefined text.
#It is a powerfull technique
#Here you have to first type "f" at the start of a string where u have to format
#Here curly braces are used to place the predefined string
#Here you can use "r" to Radant the escape characters commands.

my_name = "Vibhu Dixit"
give_name = f"My name is: {my_name}"
print(give_name)

print("Sum of 2 and 6 is: {2+6}")
print(f"Sum of 2 and 6 is: {2+6}")
print("Sum of 2 and 6 is: \n{2+6}")
print(r"Sum of 2 and 6 is: \n{2+6}")    #No \n Acts


'''Formatting In String
------------------------
{} --> replacement operator
f  --> formatting
r  --> raw
'''
