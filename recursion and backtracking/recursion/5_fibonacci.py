# Fibonacci series 1 1 2 3 5 8 ...

def main():
    n = int(input())
    fibo = fibonacci(n)
    print(fibo)

def fibonacci(n): 
  
    if n==0 or n==1:
        return 1
    # fibonacci(8)=fibonacci(6)+fibonacci(7)
    fibn =fibonacci(n-2)+fibonacci(n-1)
    # print(fibn)
    return fibn

main()
