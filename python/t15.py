sampl = ['abc', 'xyz', 'aba', '1221']
l = len(sampl)
count = 0
for i in sampl:
    if l > 2 and i[0] == i[-1]:
        count = count+1
print(count)
