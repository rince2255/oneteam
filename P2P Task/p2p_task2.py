def print_pattern():

    p_row = int(input("enter the number of rows : "))

    for i in range(0, p_row):
        for j in range(0, i+1):
            print("* ", end="")
        print()

    for i in range(p_row, 0, -1):
        for j in range(0, i-1):
            print("* ", end="")
        print()

print_pattern()
