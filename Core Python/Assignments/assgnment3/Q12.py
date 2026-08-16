#Write a program to check if given 3 digit number is a palindrome or not.
num = int(input("Enter a 3-digit number: "))

first_digit = num // 100
last_digit = num % 10

if first_digit == last_digit:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")