rows = 5

i = 1
while i <= rows:

    # Print Leading Spaces
    space = 1
    while space <= rows - i:
        print(" ", end=" ")
        space = space + 1

    # Print Increasing Numbers
    num = 1
    while num <= i:
        print(num, end=" ")
        num = num + 1

    # Print Decreasing Numbers
    num = i - 1
    while num >= 1:
        print(num, end=" ")
        num = num - 1

    print()
    i = i + 1