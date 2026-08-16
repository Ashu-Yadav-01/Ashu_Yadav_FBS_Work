#WAP to print factorial of a number .
#Factorial is the multiplication of all positive integers from 1 to a given number.
num = int(input('Enter num: '))
fact = 1
i = 1

while(i <= num):
    fact = fact * i
    i = i + 1
print(fact)