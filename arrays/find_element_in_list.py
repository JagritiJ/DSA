def find_d(mylist, d):
    if d in mylist:
        for i in range(0, len(mylist)):
            if mylist[i] == d:
                return i
    else:
        return -1

if __name__ == "__main__":
    n = int(input())
    mylist = [int(input()) for i in range(n)]
    d = int(input())
    result = find_d(mylist, d)
    print(result)

