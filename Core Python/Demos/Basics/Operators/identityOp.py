##Identity operators are used to check whether two variables refer to the same object in memory or not. Python has two identity operators: is and is not.

#is returns True if both variables point to the same memory location.
#is not returns True if both variables point to different memory locations.

x = 10 
y = 10
z = 20 
li1 = [10, 20, 30, 40 ]
li2 = [10, 20, 30, 40 ]


#1. is -  Checks whether two variables refer to the same object in memory.
print(x is y )
print(id(x))
print(id(y))
print(li1 is li2)
print(id(li1))
print(id(li2))

#2. is not --- Checks whether two variables refer to different objects in memory.
print(li1 is not li2)
print(x is not y)