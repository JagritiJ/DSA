# to print the upper traingle, use concept of gap
def upper_triangle(mylist, rows, cols):
    for gap in range(0, rows):
        for row in range(0, rows):
            col = row+gap
            if col<cols:
                print(mylist[row][col])
    #             now for the last diagonal, there is only one element


def main():
    rows = int(input())
    cols = int(input())
    mylist = [[int(input())for col in range(0, cols)] for row in range(0, rows)]

    upper_triangle(mylist, rows, cols)

main()
