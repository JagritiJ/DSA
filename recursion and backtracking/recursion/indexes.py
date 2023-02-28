def first_index(mylist, idx, data):
    if idx == len(mylist) - 1:
        return -1
    if mylist[idx] == data:
        return idx
    else:
        fi = first_index(mylist, idx + 1, data)
        return fi


def main():

    n = int(input())
    mylist = [int(input()) for i in range(n)]
    data= int(input())

    fi = first_index(mylist, 0, data)
    print(fi)


main()