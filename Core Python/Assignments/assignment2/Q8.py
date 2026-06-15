#Write a program to swap two numbers using third variable.
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print('Before Swapping')
print('x =', x)
print('y =', y)

z = x
x = y
y = z

print("After Swapping")
print("x =", x)
print("y =", y)