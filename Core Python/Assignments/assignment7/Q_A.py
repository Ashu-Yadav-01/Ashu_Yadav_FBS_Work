rows = 5
i = 1

while i <= (2 * rows - 1):

    if i <= rows:
        temp = i
    else:
        temp = 2 * rows - i

    j = 1
    while j <= rows + temp - 1:

        if j == rows - temp + 1 or j == rows + temp - 1:
            print("*", end="")
        else:
            print(" ", end="")

        j = j + 1

    print()
    i = i + 1