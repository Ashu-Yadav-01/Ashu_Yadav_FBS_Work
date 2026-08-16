#WAP to check if given number Strong Number.
n = int(input("Enter number: "))

original = n
sum = 0

while n > 0:

    digit = n % 10

    fact = 1
    i = 1

    while i <= digit:
        fact = fact * i
        i = i + 1

    sum = sum + fact

    n = n // 10

if sum == original:
    print("Strong Number")
else:
    print("Not Strong Number")