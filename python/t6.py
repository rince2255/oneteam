string = input("Enter the string : ")
if len(string) > 2:
    print(string[:2] + string[-2:])
else:
    print("Empty string")
