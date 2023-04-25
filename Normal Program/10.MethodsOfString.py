'''Methods Of String
--------------------
   1. split("pattern") -->split into several part based on pattern.
                          It returns a list. '''

x = "My name is Vibhu, I am 19 year old, I am persuing BTech from GLA, I love my mom"
print(x.split(','))     #splitting on the basis of ','
print(x.split(' '))     #splitting on the basis of ' '

'''2. ("Pattern").join(variable_name) -->join the string on the bases of pattern'''
                                    #It coverts list into string.
x = ["My name is Vibhu", "I am 19 year old", "I am persuing BTech from GLA", "I love my mom"]
print(','.join(x))      #joining on the basis of ','
print(' '.join(x))      #joining on the basis of ' '

'''3. variable_name.find("pattern","start","end") -->Find the position of our pattern
                                        If pattern not fount return -1.'''

x = "a quick brown fox jump over the lazy dog"
print(x.find('quick'))      #2
print(x.find('vibhu'))      #-1
print(x.find('o',12,-1))    #15

'''4. variable_name.index("pattern","start","end") -->same as find
                                        But it will return error when no pattern found.'''


x = "a quick brown fox jump over the lazy dog"
print(x.index('quick'))      #2
#print(x.index('vibhu'))      #error
print(x.index('o',12,-1))    #15
                                
'''5. count("pattern","start","end") -->return no. of occurrence of species'''

x = "Vibhu is best. Vibhu loves kashish."
print(x.count('Vibhu'))     #2
print(x.count('kallo'))     #0

'''6. strip() -->remove leading and trailing spaces'''

x =  "          My name is Vibhu            "
print(x.strip())

'''7. replace("old name","new name") --> replace older with new'''

x = "Vibhu is best. Vibhu loves kashish."
print(x.replace("Vibhu","Raj"))