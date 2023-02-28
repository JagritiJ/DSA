# https://www.youtube.com/watch?v=YWXbu5uyGXs&list=PL-Jc9J83PIiHq5rMZasunIR19QG3E-PAA&index=10

def main():
    mylist = list(map( int, input().split() ))

    longest_increasing_sequence(mylist)

def longest_increasing_sequence(mylist):
    mydict = dict()
    #  first loop, set true everywhere
    for i in range(0, len(mylist)):
        # make sure every unqiue item is only entered in the dictionary
        if mylist[i] not in mydict.keys():
            mydict[mylist[i]] = True

    # now loop over mydict and see for every value can I find a smmaller value, if yes, set this to false
    # considering, this definitely is not the start of the series
    # print(len(mydict))
    for key in mydict.keys():
        # if you find key-1 as a val for another key
        if key-1 in mydict.keys():
            # set this particular item as false, as this is not the start of the series
            mydict[key] = False
    
    print(mydict)
    #     10 5 9 1 11 8 6 5 3 12 2
    # {10: False, 5: True, 9: False, 1: True, 11: False, 8: True, 6: False, 3: False, 12: False, 2: False}
    # by now we have got the necessary dict with True values, now just iterate obver them

# Now this sounds like a nexted loop ? 
    for key in mydict.keys():
        if mydict[key] == True:
            print(key)
            while key+1 in mydict.keys():
                print(key+1)
                key=key+1

# perfect answer, but double loop
# 5
# 6
# 1
# 2
# 3
# 8
# 9
# 10
# 11
# 12
         
main()