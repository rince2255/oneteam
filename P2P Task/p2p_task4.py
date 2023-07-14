def cal_weightage(my_string):
    sum_string = 0
    for ch in my_string:
        sum_string = sum_string + ord(ch.upper()) - 64
    return sum_string


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


my_list = ['b', 'bc', 'cd', 'bbbbb']
prime_list = []
for words in my_list:
    cal_weightage(words)
    if is_prime(cal_weightage(words)):
        prime_list.append(words)

print("The strings with prime weightage are : \n", prime_list)
