username = 'admin'
password = '000'

userid = input('Enter Userid:')
passw = input('Enter Password:')

if(username == userid and password == passw):
    print('Logged in Successful.')
else:
    print('Invalid Credentials.')    