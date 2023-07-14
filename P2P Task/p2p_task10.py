
def print_descending(limit):
    i = limit
    while i >= 1:
        print(i, end=", ")
        i = i-1


limit = int(input("Enter the limit : "))
print_descending(limit)

