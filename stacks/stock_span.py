# https://www.youtube.com/watch?v=0BsPlzqksZQ&list=PL-Jc9J83PIiEyUGT3S8zPdTMYojwZPLUM&index=10

def main():
    stock = list(map(int, input().split()))
    stack = list()
    span = list()

    for i in range(0, len(stock)):
        if len(stack) == 0:
            # index
            stack.append(i)
            # just index if nothing bigger encountered
            span.append(i+1)
        else:
            # peek = stock[stack[-1]]:
            while(len(stack) >0 and stock[i] > stock[stack[-1]]):
                # pop
                stack = stack[-1]
            
            if len(stack) ==0:
                span.append(i+1)
            else:
                # stock[i] <= stock[stack[-1]]:
                span.append(i - stack[-1] )

            stack.append(i)
main()