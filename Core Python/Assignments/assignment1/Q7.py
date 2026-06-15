#Program to Find the Roots of a Quadratic Equation
import math

a = int(input('Enter the number a: '))
b = int(input('Enter the number b: '))
c = int(input('Enter the number c: '))



d = (b * b ) - (4 * a * c )

root1 = (- b + math.sqrt(d)) / 2 * a
root2 = (- b - math.sqrt(d)) / 2 * a

print('d: ', d)
print('Root 1 is: ', root1)
print('Root 2 is: ',root2)