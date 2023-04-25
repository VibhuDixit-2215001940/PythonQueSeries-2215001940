#The Number In The Form Of a+bj Is Comes Under Complex Data Type
#Where a => real part (integer/float) (can be hex, bin, dec, oct)
#Where b => imaginary part (integer/float) (can only be dec)

#Function Used To Accessed The Real And Imaginary Part Are:-
#real() ==> return real part of numbers
#imag() ==> return imaginary part of numbers
#Its Syntax Is:- variableName.real , variableName.imag
 
var = 20 + 50j
print(type(var))        #<class 'complex'>
print(var.real)         #20.0
print(var.imag)         #50.0


x = 0b1111 + 32.0j
print(type(x))        #<class 'complex'>
print(x.real)         #15.0
print(x.imag)         #32.0




