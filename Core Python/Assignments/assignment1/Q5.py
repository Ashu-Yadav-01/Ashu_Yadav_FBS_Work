#Question 5: Write a program to calculate Compound Interest.
p = int(input('Enter the principle: '))
r = int(input('Enter the rate: '))
t = int(input('Enter the time: '))

ci = p * ((1 + r / 100) ** t) - p

print('Compound Intrest :', ci)