# https://www.youtube.com/watch?v=KruULhITtk4&list=PL-Jc9J83PIiHq5rMZasunIR19QG3E-PAA&index=4

def main():

    mylist1 = [1, 1, 1, 2, 2, 2, 3, 5]
    mylist2 = [1, 1,1, 1, 2,2,4,5]

    mydict = dict()

    # First store items in dict by taking input from list 1. 
    # After that just iterate ofver list 2 and see keys from dict match the list2
    for num in mylist1:

        if mydict.get(num) == None:
            mydict[num] = 1
        else:
            mydict[num] = mydict.get(num)+1

    common_list=set()
    for num in mylist2:
        # print(num)
        if num in mydict.keys():
            # print(num)
            common_list.add(num)

    print(common_list)
main()