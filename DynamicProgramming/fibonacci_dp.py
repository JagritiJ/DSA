
def fibonacci_memo(n, dp):
    
    if n<=1: 
        dp[n] = n
        return dp[n]

    if dp[n] !=0:
        return dp[n]
    
    fibn = fibonacci_memo(n-1, dp)+fibonacci_memo(n-2, dp)
    dp[n] = fibn
    return dp[n]

def display(dp):
    for ele in dp:
        print (ele)

def main():
    n = 10
    dp =[]
    # in python initialize the list
    dp =[0] * (n+1)
    answer = fibonacci_memo(n, dp)
    print(answer)
    display(dp)

main()