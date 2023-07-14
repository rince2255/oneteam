def find_factorial(my_num):
    if my_num < 0:
        print("Please enter a number equal to or greater than zero")
    elif my_num == 0:
        return 1
    else:
        return (my_num*(find_factorial(my_num-1)))


my_num = int(input("Enter the number to find factorial : "))

result = find_factorial(my_num)
print("The factorial of", my_num, "is", result)
