#Write a program to calculate profit or loss.
cp = int(input('Enter the CP: '))
sp = int(input('Enter the Sp: '))

amount = sp - cp

if (amount > 0):
    print('profit',amount)
elif(amount == 0):
    print('No profit')
else:
    print('loss', amount)    