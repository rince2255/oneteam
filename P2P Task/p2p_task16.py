def calculate_lcm(num1,num2):
    if num1>num2:
        higher=num1
    else:
        
        higher=num2
    value=higher
    while True:

        if (higher%num1==0 and higher%num2==0):
            print("LCM of",num1,"and",num2,"is",higher)
            break
        else:
            higher=higher+value
num1=int(input("Enter the first number : "))
num2=int(input("Enter the second number : "))
calculate_lcm(num1,num2)
