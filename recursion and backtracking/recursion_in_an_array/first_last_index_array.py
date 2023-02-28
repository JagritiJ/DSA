# Program to find the first and the last index of an element in an array
import sys
# sys.setrecursionlimit(1000000)

def first_last_indexes(arr, idx, n, x):
    if idx == n:
        return -1
    if x==arr[idx]:
        return idx
    else:
       fiisa = first_last_indexes(arr, idx + 1, n, x)
    return fiisa

def last_index(arr, idx, n, x):
    if idx == n:
        liisa = -1

    liisa = last_index(arr, idx + 1, n, x)

    if liisa ==-1:
        if arr[idx] == x:
            return idx
        else:
            return -1
    else:
        return liisa
#     check base case if the item is not prezent

def main():
    # limit = sys.getrecursionlimit()
    # print(limit)  -- 1000
    arr = list()
    n = int(input())
    for i in range(0,n):
        arr.append(int(input()))
    x = int(input())
    # fi = first_last_indexes(arr, 0, n, x)
    # print(fi)
    li = last_index(arr, 0, n, x)
    print(li)

main()