from itertools import groupby


def data_compression(string):
    result = []
    s = ""
    for char, group in groupby(string):
        length = len(list(group))
        length_ = str(length)
        if int(length_) <= 1:
            length_ = ""
        result.append((char, length))
        s = s + "".join(char+length_)
    print(s)
    return result


d = input("String to be compressed: \n\n")
print("\nCompressed string : \n")
data_compression(d)
