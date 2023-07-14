# def find_sum(nuns, input):
#     for i in range(len(nuns)):
#         for j in range(i+1, len(nuns)):
#             if nuns[i] + nuns[j] == input:
#                 return [nuns[i], nuns[j]]

# nuns = [1, 2, 7, 11]
# input = 9
# output = find_sum(nuns, input)
# print(output)

nuns = [1, 2, 7, 11]
input = int(input("Enter the target number : "))
output = []

for i in range(len(nuns)):

    for j in range(i+1, len(nuns)):
        if nuns[i] + nuns[j] == input:
            output.append(i)
            output.append(j)
# nuns = [nuns[i]for i in range(len(nuns)) if i not in output]
print(input, "=", output)
print(output)
print(nuns)
