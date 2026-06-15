#Find the sum of three-digit number.
num = int(input('Enter 3 digit number: '))

d1 = num % 10
num = num // 10

d2 = num % 10
num = num // 10

d3 = num % 10
num = num // 10

sum = d1 + d2 + d3

print('sum of three digit number: ',sum)