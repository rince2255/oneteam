def check_strings(master_string, string1, string2):
    if string1 in master_string:
        master_string = master_string.replace(string1, "")
        print(string1 + ": yes")
        print(master_string)
    else:
        print(string1 + ": no")

    if string2 in master_string:
        print(string2 + ": yes")
    else:
        print(string2 + ": no")


master_string = "aabcglactdde"
string1 = input("Enter string1: ")
string2 = input("Enter string2: ")


check_strings(master_string, string1, string2)
