'''Write a program to prompt user to enter userid and password. After verifying
userid and password display a 4 digit random number and ask user to enter the
same. If user enters the same number then show him success message otherwise
failed. (Something like captcha)  '''
import random

username  = input('Enter the Username:')
password = int(input('Enter the password :'))

if username == 'admin' and password == 1234 :
    captcha = random.randint(1000, 9999)
    print("Captcha:", captcha)

    user_captcha = int(input('Enter the captcha: '))

    if user_captcha == captcha:
        print('Login Successful')
    else:
        print('Captcha verification Failed')
else:
    print('Invalid username or Password')        

