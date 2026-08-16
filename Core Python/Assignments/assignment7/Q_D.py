rows = 5

i = 1
while i <= rows:

    space = 1
    while space <= rows - i:
        print(" ", end=" ")
        space = space + 1

    num = i 
    j = 1
    while j <= i:
        print(num, end=" ")
        num = num + 1
        j = j + 1

    num = num - 2
    j = 1
    while j <= i - 1:
        print(num, end=" ")
        num = num - 1
        j = j + 1

    print()
    i = i + 1             