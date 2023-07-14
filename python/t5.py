mstring = "kundddddannnnnn"
mydict = {}
for n in mstring:
    keys = mydict.keys()
    if n in keys:
        mydict[n] += 1
    else:
        mydict[n] = 1
print(mydict)
