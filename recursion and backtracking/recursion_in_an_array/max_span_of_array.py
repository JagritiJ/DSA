def max_of_array(arr, start, n):
    if start == n-1:
        return arr[start]
    misa = max_of_array(arr, start+1, n)
    if arr[start]> misa:
        return arr[start]
    else:
        return misa


def main():
    arr = list()
    n = int(input())
    for i in range(0,n):
        arr.append(int(input()))
    mymax = max_of_array(arr, 0, n)
    print(mymax)
main()