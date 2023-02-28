# https://www.youtube.com/watch?v=ea8L1x_JSvM&list=PL-Jc9J83PIiHq5rMZasunIR19QG3E-PAA&index=3

import math
def main():

    # mylist = list(input().split())
    mylist = ["a", "a", "d", "d", "d",]
    # Creating a dictionary
    mydict = dict()
    for ch in mylist:
        # print(ch)
        # print(mydict.get(ch))
        if (mydict.get(ch) == None):
            mydict[ch] = 1
        else:
            mydict[ch] = mydict.get(ch)+1
    print(mydict.items())

    max_val = -math.inf
    for key in mydict.keys():
        max_val = max(max_val, mydict[key])

    print(max_val)

main()

