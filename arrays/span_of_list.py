
def span(mylist):
    mylist_sorted = mylist.sort()
    return abs(mylist[len(mylist ) -1] - mylist[0])

if __name__ == "__main__":
    n = int(input())
    mylist = [int(input()) for i in range(n)]

    result = span(mylist)
    print(result)