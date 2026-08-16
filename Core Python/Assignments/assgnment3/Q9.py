#Input 5 subject marks from user and display grade(eg.First class,Second class ..)
sub1 = float(input('Enter marks of Maths:'))
sub2 = float(input('Enter marks of English:'))
sub3 = float(input('Enter marks of Marathi:'))
sub4 = float(input('Enter marks of Hindi:'))
sub5 = float(input('Enter marks of Science:'))

total = sub1 + sub2 + sub3 + sub4 + sub5 
percentage = (total / 500) * 100

if percentage >= 60:
    print('First Class')
elif percentage >= 50:
    print('Second Class')
elif percentage >= 35:
    print('Pass')
else:
    print('Fail')            