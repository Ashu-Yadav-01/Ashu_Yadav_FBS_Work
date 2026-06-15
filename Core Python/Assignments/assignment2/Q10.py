#Write a program to reverse three-digit number.
''' Logic 
digit1 = number // 100
digit2 = (number % 100) // 10
digit3 = number % 10

reverse = (digit3 * 100) + (digit2 * 10) + digit1 '''

num = int(input("Enter a three-digit number: "))

digit1 = num // 100
digit2 = (num % 100) // 10
digit3 = num % 10

reverse = (digit3 * 100) + (digit2 * 10) + digit1

print("Reverse Number =", reverse)