def ceil_and_floor(denomination, mylist):
    ceil = 0
    floor = 0
    low = 0
    high = len(mylist) - 1
    while (low <= high):
        mid = int( (low + high) / 2)
        if denomination < mylist[mid]:
            high = mid - 1
            ceil = mylist[mid]
        elif denomination > mylist[mid]:
            low = mid + 1
            floor = mylist[mid]

        else:
            ceil = mylist[mid]
            floor = mylist[mid]
            break
    print(ceil)
    print(floor)

def main():
    n = int(input())
    count = 0
    mylist = [int(el) for el in input().split()]
    denomination = int(input())
    ceil_and_floor(denomination, mylist)

main()