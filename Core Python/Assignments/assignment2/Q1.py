#Question 12: Write a program to convert time into seconds.
hours = int(input('Enter the hours: '))
minute = int(input('Enter the Minute: '))
seconds = int(input('Enter the seconds: '))

total_seconds = (hours * 3600) + (minute * 60) + seconds

print('Total seconds: ',total_seconds)