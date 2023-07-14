limit=int(input("Enter the rows : "))
for rows in range(limit):
    num=rows+1
    incriment=limit+2

    for j in range(rows+1):
        print(num ,end=" ")
        num=num+incriment
        incriment=incriment-1
    print()



   