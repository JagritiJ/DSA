# Program for factorial of n
def power_linear(x, n):

    if n ==0:
        return 1
    # fn minus 1, faith
    plm1 = power_linear(x, n-1)
    # matching expectation and faith
    pl = x * plm1

    return pl

def main():
    x = int(input())
    n = int(input())

    result = power_linear(x,n)
    print(result)
main()