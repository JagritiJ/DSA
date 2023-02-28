def wave(mylist, rows, cols):
    row = 0
    for col in range(0, cols):
        if col % 2 == 0:
            for row in range(0, rows, 1):
                print(mylist[row][col])

        else:
            for row in range(rows-1, -1, -1):
                print(mylist[row][col])


def main():
    rows = int(input())
    cols = int(input())

    mylist = [[int(input()) for col in range(cols)] for row in range(rows)]

    wave(mylist, rows, cols)


main()