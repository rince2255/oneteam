def print_pattern():

    limit = int(input("Enter number of rows : "))

    for i in range(1,limit+1):
        for j in range(1, i+1):
            print(j%2, end="")
        print()

print_pattern()