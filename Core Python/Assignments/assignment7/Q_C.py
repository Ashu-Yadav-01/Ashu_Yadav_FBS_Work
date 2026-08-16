rows = 5

i = 1
while i <= rows:

    j = 1
    while j <= i:

        if j == 1 or j == i or i == rows:
            print(j, end=" ")
        else:
            print(" ", end=" ")

        j = j + 1

    print()
    i = i + 1