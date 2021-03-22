# Various star formations and printing the same in python

def print_square(n):
    nst = n
    rows = n
    for row in range(rows):
        for cst in range(nst):
            print("*", end="")
        nst = n
        print("\n")

def print_triangle(n):
    nst = 1
    rows = n
    for row in range(rows):
        for cst in range(nst):
            print("*", end="")
        nst +=1
        print("\n")

def inverse_triangle(n):
    nst = n
    rows = n
    for row in range(rows):
        for cst in range(nst):
            print("*", end="")
        print("\n")
        nst -=1

def side_triangle(n):
    print("hi")
    nst = 1
    nsp = n-1
    rows = n
    for row in range(rows):
        for csp in range(nsp):
            print(" ", end="")
        for cst in range(nst):
            print("*", end="")
        nsp-=1
        nst+=1
        print("\n")

def half_diamond(n):
    nst = 1
    nsp = n - 1
    rows = n
    for row in range(rows):
        for csp in range(nsp):
            print(" ", end="")
        for cst in range(nst):
            print("*", end="")

        nsp -= 1
        nst += 2
        print("\n")

def full_diamond(n):
    # here n has to be odd number, nsp has to be related to the n
    nst = 1
    nsp = int(n/2)
    rows = n
    for row in range(rows):
        for csp in range(nsp):
            print(" ", end="")
        for cst in range(nst):
            print("*", end="")
        if(row<int(n/2)):
            nsp -= 1
            nst += 2
        else:
            nsp += 1
            nst -= 2
        print("\n")

def hollow_diamond(n):
    nsp = int(n/2)
    nst = 1
    rows =n
    for row in range(rows):
        for csp in range(nsp):
            print("*", end="")
        for cst in range(nst):
            print(" ", end="")
        for csp in range(nsp):
            print("*", end="")
        if(row<int(n/2)):
            nsp -= 1
            nst += 2
        else:
            nsp += 1
            nst -= 2
        print("\n")

def number_diamond(n):
    # here n has to be odd number, nsp has to be related to the n
    nst = 1
    nsp = int(n/2)
    rows = n
    val =0
    for row in range(rows):
        for csp in range(nsp):
            print(" ", end="")

        if row <n/2: val=val +1
        else: val= n-row

        for cst in range(nst):
            print(val, end="")
        if(row<int(n/2)):
            nsp -= 1
            nst += 2
        else:
            nsp += 1
            nst -= 2
        print("\n")

def mix_number_diamond(n):
    # here n has to be odd number, nsp has to be related to the n
    nst = 1
    nsp = int(n/2)
    rows = n
    val =0
    for row in range(rows):
        for csp in range(nsp):
            print(" ", end="")

        if row <n/2: val=val +1
        else: val= n-row

        for cst in range(nst):
            print(val, end="")
        if(row<int(n/2)):
            nsp -= 1
            nst += 2
        else:
            nsp += 1
            nst -= 2
        print("\n")

if __name__ == "__main__":
    n = int(input())
    print("Printing Square\n", print_square(n))
    print("Printing Triangle\n", print_triangle(n))
    print("Printing Inverse Triangle\n", inverse_triangle(n))
    print("Side Triangle\n", side_triangle(n))
    print("Half Diamond\n", half_diamond(n))
    print("Full Diamond\n", full_diamond(n))
    print("Hollow Diamond\n", hollow_diamond(n))
    print("Number Diamond\n", number_diamond(n))
    print("Mix Number Diamond\n", mix_number_diamond(n))