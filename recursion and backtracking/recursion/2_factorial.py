# Program for factorial of n
def factorial(n):

    if n ==1:
        return 1
    # fn minus 1, faith
    fnm1 = factorial(n-1)
    # matching expectation and faith
    fn = n * fnm1

    return fn

def main():
    n = int(input())
    result = factorial(n)
    print(result)
main()