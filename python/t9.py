str1 = input("Enter your string : ")
length = len(str1)
ing = "ing"
ly = "ly"
if length>=3:
    if str1[-3:] == ing:
        str1 = str1 + ly
    else:
    
        str1 = str1 + ing

print(str1)
