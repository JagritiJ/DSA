def rotate90(mylist, rows, cols):
    # basically print column wise and revere
    rmin = 0
    rmax = rows - 1
    cmin = 0
    cmax = cols - 1
    new_list = list()
    output_list = list()
    for col in range(cmin, cmax + 1):
        for row in range(rmax, rmin - 1, -1):
            new_list.append([mylist[row][col]])
            print(mylist[row][col])

    for i in range(0, rows):
        for j in range(0, cols):
            print(new_list[i][j])
        print("\n")

def main():
    rows = cols = int(input())
    mylist = [[int(input()) for col in range(0, cols)] for row in range(0, rows)]

    rotate90(mylist, rows, cols)


main()