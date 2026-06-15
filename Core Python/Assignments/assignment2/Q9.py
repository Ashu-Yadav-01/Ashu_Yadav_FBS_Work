#Write a program to swap two numbers without using third variable.
''' Logic
x = x + y
y = x - y
x = x - y'''

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Before Swapping")
print("x =", x)
print("y =", y)

x = x + y
y = x - y
x = x - y

print("After Swapping")
print("x =", x)
print("y =", y)