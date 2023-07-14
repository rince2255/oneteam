for i in range(1, 8):
    for j in range(1, 15):
        if j == 8 - i or j == 8 + i:
            print('O', end='')
        elif i > 1 and (j == 6 - i or j == 10 + i):
            print('N', end='')
        elif i > 2 and (j == 4 - i or j == 12 + i):
            print('E', end='')
        elif i > 3 and (j == 2 - i or j == 14 + i):
            print('T', end='')
        elif i > 4 and (j == 1 or j == 15):
            print('A', end='')
        else:
            print(' ', end='')
    print()