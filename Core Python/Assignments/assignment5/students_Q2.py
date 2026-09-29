n = int(input("Enter number of students: "))

i = 1
total_percentage = 0

while i <= n:

    print("Enter marks for Student", i)

    j = 1
    total = 0

    while j <= 5:
        marks = int(input("Enter marks: "))
        total = total + marks
        j = j + 1

    percentage = total / 5

    print("Percentage:", percentage)

    total_percentage = total_percentage + percentage

    i = i + 1

average = total_percentage / n

print("Average Percentage:", average)