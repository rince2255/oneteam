def print_pattern():
    p_row = int(input("Enter the number of rows : "))
    for i in range(p_row, 0, -1):
        for j in range(p_row-i):
            print("  ", end="")
        for j in range(1, 2*i):
            print("* ", end="")
        print()

    for i in range(2, p_row+1):
        for j in range(p_row-i):
            print("  ", end="")
        for j in range(1, 2*i):
            print("* ", end="")
        print()

print_pattern()