#Write a program to check if the given number is positive or negative.
number = int(input('Enter the Number: '))

if number > 0 :
    print('Number is Positive', number)
#else: 
#    print('Number is negative', number)
elif number < 0 :
    print('Number is Negative',number)
else:
    print('Zero')