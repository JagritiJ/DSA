def search_in_sorted_twod(mylist, rows, cols, item):
    for i in range(0, rows):
        for j in range(0, cols):
            if item == mylist[i][j]:
                print(i)
                print(j)
                return

    return "Not Found"


def main():
    rows = cols = int(input())

    mylist = [[int(input()) for col in range(0, cols)] for row in range(0, rows)]
    item = int(input())

    search_in_sorted_twod(mylist, rows, cols, item)


main()