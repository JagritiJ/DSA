def spiral(mylist, rows, cols):
    rmin = 0
    cmin = 0
    rmax = rows - 1
    cmax = cols - 1
    total = rows * cols
    count =0
    while( count<total ):
        for row in range(rmin, rmax + 1):
            if count<total:
                print(mylist[row][cmin])
                count+=1
        cmin += 1

        for col in range(cmin, cmax + 1):
            if count<total:
                print(mylist[rmax][col])
                count+=1
        rmax -= 1

        for row in range(rmax, rmin+1, -1):
            if count<total:
                print(mylist[row][cmax])
                count+=1
        cmax -= 1
        for col in range(cmax, cmin+1, -1):
            if count<total:
                print(mylist[rmin][col])
                count+=1
        rmin += 1


def main():
    rows = int(input())
    cols = int(input())
    mylist = [[int(input()) for col in range(0, cols)] for row in range(0, rows)]

    spiral(mylist, rows, cols)


main()