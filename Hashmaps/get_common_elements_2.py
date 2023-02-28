# https://www.youtube.com/watch?v=hBX47E5WDIA&list=PL-Jc9J83PIiHq5rMZasunIR19QG3E-PAA&index=6

a1 = [1,1,2,2,2,3,5]
a2 = [1,1,1,2,2,4,5]

# Solution = [1,1,2,2,5] - selevcting from 2nd list, as 4 isn't present in list1, we ignored it
# so this means outer lloop is for a2, or we can make dictionary for a2

mydict = dict()

for i in range(0, len(a2)):
    if a2[i] in mydict.keys():
        mydict[a2[i]] = mydict[a2[i]] +1
    else:
        mydict[a2[i]] = 1

print("mydict.items() ", mydict.items())

# We now have freq map for a2.

# now for common elements in a2 from a1
for i in range(0, len(a1)):
    if a1[i] in mydict.keys():
        # too make sure the count observed is of the a2
        # to make sure it doesn't prinyts values <=0
        if mydict[a1[i]] > 0:
            mydict[a1[i]] = mydict[a1[i]] -1
            print(a1[i])

# answer
# 1
# 1
# 2
# 2
# 5