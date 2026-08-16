#Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.
a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

if a == b and  b == c :
    print('Equilateral')
elif a == b or a == c or b == c:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")
