#Question 7: Write a program to convert total days into Years, Weeks, and Days.
days = int(input('Enter the Days: '))

years = days // 365
days  = days % 365

Week = days // 7
days = days % 7

print('Years: ', years)
print('Weeks: ', Week)
print('days: ', days)