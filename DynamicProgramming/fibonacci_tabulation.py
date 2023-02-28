def display(dp):
    for ele in dp:
        print (ele)

def fibonacci_memo(n, dp):
    
    for i in range(0, n):
        if n<=1: 
            dp[n] = n
    
    # fibonacci_memo(n-1, dp)+fibonacci_memo(n-2, dp)
    dipn = dp[n-1]+dp[n-2]
    dp[n] = dipn
    return dp[n]

def main():
    n = 10
    dp =[]
    # in python initialize the list
    dp =[0] * (n+1)
    answer = fibonacci_memo(n, dp)
    print(answer)

main()