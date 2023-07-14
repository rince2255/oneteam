str1 = "abc"
str2 = "xyz"
char1 = str1[0:2]
char2 = str2[0:2]
str1 = str1.replace(char1, char2)
str2 = str2.replace(char2, char1)
x = str1+str2
print(x)
