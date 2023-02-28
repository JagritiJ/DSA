# Program for factorial of n, now in log n time, by changing the faith
def power_log(x, n):

    if n == 0:
        return 1
    # fn minus 1, faith
    plm1 = power_log(x, int(n/2))
    pl = plm1 * plm1

    # matching expectation and faith
    if n%2 == 1:
        pl = x * pl

    return pl

def main():
    x = int(input())
    n = int(input())

    result = power_log(x,n)
    print(result)
main()