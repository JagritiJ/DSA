import sys

def wakanda1(mylist):
    pass

def wakanda2(mylist):
    pass

def spiral(n, m, mylist):
    tnel = n*m
    rmin=0
    rmax=n-1
    cmin=0
    cmax=m-1

    while tnel>0:
        for row in range(rmin, rmax+1):
            if tnel >0:
                print(mylist[row][cmin])
                tnel-=1
        cmin +=1
        for col in range(cmin, cmax+1):
            if tnel > 0:
                print(mylist[rmax][col])
                tnel-=1
        rmax-=1
        for row in range(rmax, rmin, -1):
            if tnel > 0:
                print(mylist[row][cmax])
                tnel -= 1
        cmax -=1
        for col in range(cmax, cmin, -1):
            if tnel > 0:
                print(mylist[rmax][col])
                tnel -= 1

def exitPoint(n,m,mylist):
    i=0
    j=0

    dir=0
    while(True):
        dir = (dir + mylist[i][j]) % 4
        # East
        if dir ==0:
            j=j+1
            if j==m:
                print(i)
                print(j-1)
                break
        # North
        if dir ==1:
            i=i+1
            if i==n:
                print(i-1)
                print(j)
                break
        # West
        if dir ==2:
            j=j-1
            if j==-1:
                print(i)
                print(j+1)
                break
        # South
        if dir ==3:
            i=i-1
            if i==-1:
                print(i+1)
                print(j)
                break

def saddle_point(n, m, mylist):
#     find min in row and max in col
    min_row =list()
    min_val = sys.maxsize
    for i in range(n):
        min_row.append([[min(min_val, mylist[i][j]), i, j] for j in range(m)])
    max_val = -sys.maxsize
    max_col=-1
    for j in min_row:
        max_col =[max(max_val, mylist[j[0][1]][j[0][2]], i, j) for i in range(n)]

    print(min_row)
    print(max_col)



if __name__ == "__main__":
    n = int(input())
    m = int(input())
    mylist = [[int(input())  for j in range(m)]for i in range(n)]
    # print(mylist)
    # result = wakanda1(mylist)
    # spiral(n, m, mylist)
    # print(result)
    # exitPoint(n, m, mylist)
    saddle_point(n, m, mylist)
