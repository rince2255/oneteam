n = int(input("Enter your input\n"))
word_list = []
for i in range(n):
    word_list.append(input())

New_word_list = []
for element in word_list:
    if element in New_word_list:
        New_word_list = New_word_list
    else:
        New_word_list.append(element)

print(len(New_word_list))
for element in New_word_list:
    print(word_list.count(element), end=" ")
