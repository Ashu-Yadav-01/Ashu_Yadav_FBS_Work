#WAP to check if a given number is prime number or not.
n = int(input("Enter number: "))

i = 2
flag = 0

while i < n:

    if n % i == 0:
        flag = 1
        break

    i = i + 1

if flag == 0:
    print("Prime Number")
else:
    print("Not Prime Number")