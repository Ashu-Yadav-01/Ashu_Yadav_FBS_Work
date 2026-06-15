#Question 4: Write a program to enter P, T, R and calculate Simple Interest.
p = int(input('Enter the principal amount: '))
t = int(input('Enter Time: '))
r = int(input('Enter the Rate: '))

SI = (p * t * r) / 100

print('Simple Intrest :', SI)