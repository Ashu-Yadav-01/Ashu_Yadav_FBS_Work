gender = input('Enter gender(M/F):')

age = int(input('Enter age:'))

if(gender == 'F'):
    if(age >= 18 ):
        print('Girl is eligble for marriage.')
    else:
        print('Girl is not eligble for marriage.')
else:
    if(age >= 21):
        print('Boy is eliginle for marriage.')
    else:
        print('Pahle kama lo.')            