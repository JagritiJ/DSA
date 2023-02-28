# Program to print array items in reverse order using recursion

def reversed(arr, start, n):
    if start == n:
        return
    # printing from beg to end
    print(arr[start])
    reversed(arr, start+1, n)
    # reversed order when coming down from stack
    print(arr[start])


def main():
    arr = list()
    n = int(input())
    for i  in range(n):
        arr.append(input())
    reversed(arr, 0, n)
main()