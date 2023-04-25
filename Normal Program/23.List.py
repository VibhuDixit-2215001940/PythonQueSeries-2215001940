'''LISTS-->
-----------
-It is a data structure which is also called as collection of items.
-In this we acn store anything like-string, float, integer,etc.
-SYNTAX-->list_name = [item1,item2,......]
-We write  the item of the list inside"Square Brackets"([]) and each item is separated by comma.
-Duplicates elements are allowed.
-Mutable in nature.
'''
#PRINTING LIST 
a = [10,"Kashish",12.8,"Vibhu",10]
print(a)
print(type(a))
#PRINTING ELEMENTS IN RANGE
a = [10,"Kashish",12.8,"Vibhu",10]
print(a[0:2])
#COUNTING OF ELEMENTS
a = [10,"Kashish",12.8,"Vibhu",10]
print(a.count(10))
#PRINTING WITH INDEXES
a = [10,"Kashish",12.8,"Vibhu",10]
print(a.index(10))
#INSERTING ELEMENTS 
a = [10,"Kashish",12.8,"Vibhu",10]
a.insert(2,"Nagdevv")       #.insert(index_value,"Value_to_be_inserted")
print(a)       
#DELETING ELEMENT OF INDEX
a = [10,"Kashish",12.8,"Vibhu",10]
a.pop(0)                    #pop()-->index which is to be deleted
print(a)
#EXTENDING A LIST
a = [10,"Kashish",12.8,"Vibhu",10]
b = ["Vibhu","Dixit"]
a.extend(b)
print(a)
#COPYING TWO LIST 
a = [10,"Kashish",12.8,"Vibhu",10]
c = a.copy()
print(c)
#-------------------------------------Another Method For Copying A List
a = [10,"Kashish",12.8,"Vibhu",10]
c = a[:]
print(c)
#SORTING A LIST
#a = [10,"Kashish",12.8,"Vibhu",10]
#a.sort()        #TypeError-->as all datatype are diff. so < can't be used
#print(a)
#
a = [1,78,345,98,0]
a.sort()
print(a)
#SORTING IN DESCENDING ORDER
a = [1,78,345,98,0]
a.sort(reverse=True)
print(a)
#REVERSING A LIST ELEMENTS
a = [1,78,345,98,0]
a.reverse()
print(a)
#NESTED LIST
a = [1,78,[345,["Kashish"]],98,0]
print(a)
#UNPACKING OF LISTS ELEMENTS
a = ["Vibhu","Dixit"]
x,y = a
print(x)
print(y) 

