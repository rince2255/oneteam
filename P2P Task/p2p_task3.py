def task_three():

    my_string = input("Enter any string that you want :  ")
    my_words = my_string.split()

    my_dictionary = {}
    for the_word in my_words:
        if the_word[0] not in my_dictionary:
            my_dictionary[the_word[0]] = [the_word]
        else:
            my_dictionary[the_word[0]].append(the_word)

    for k in sorted(my_dictionary.keys()):
        print(f"('{k}', ':', {my_dictionary[k]})")


task_three()
