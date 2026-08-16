row = 5

i = 1
while i <= row:


    space = 1
    while space <= row - i :
        print(" ", end="")
        space = space + 1

    j = 1
    while j <= i:

        if j == 1 or j == i or i == row:
            print(j, end= " ")
        else:
            print(" ", end=" ")

        j = j + 1

    print()
    i = i + 1                