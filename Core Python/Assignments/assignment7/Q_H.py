rows = 5

i = 1
while i <= rows:

    # Leading Spaces
    space = 1
    while space <= rows - i:
        print(" ", end=" ")
        space = space + 1

    # Increasing Numbers
    num = 1
    while num <= i:
        print(num, end=" ")
        num = num + 1

    # Middle Spaces
    if i != rows:
        space = 1
        while space <= 2 * (rows - i):
            print(" ", end=" ")
            space = space + 1

    # Decreasing Numbers
    num = i
    while num >= 1:
        if i == rows and num == i:
            num = num - 1
            continue

        print(num, end=" ")
        num = num - 1

    print()
    i = i + 1