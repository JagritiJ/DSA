import math


def isprime(n):
    max_div = math.floor(math.sqrt(n))
    for i in range(2, 1 + max_div):
        if n % i == 0:
            return False
    return True


def main():
    n = int(input())
    mylist = [int(el) for el in input().split() if not isprime(int(el))]

    if len(mylist) > n:
        return -1

    print(mylist)


main()
