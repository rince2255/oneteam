my_string = input("Enter a string: ")

count = {}

for i in my_string:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

print("Character count in the string are :")
for key, value in count.items():
    print(key, "=", value)