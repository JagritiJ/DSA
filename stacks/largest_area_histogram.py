# https://www.youtube.com/watch?v=tCVOQX3lWeI&list=PL-Jc9J83PIiEyUGT3S8zPdTMYojwZPLUM&index=14
# gives wrong answer

def main():

    arr = list(map(int, input().split()))
    stack1 = list()
    rb = list()
    stack2 = list()
    lb=list()
    maxarea =1

    rb = calculate_right_boundary(arr, stack1, rb)
    lb = calculate_left_boundary(arr, stack2, lb)

    for i in range(0, len(arr)):
        width = rb[i] - lb[i] -1
        height = arr[i]
        area = width * height
        maxarea = max(area, maxarea)

    print(maxarea)

def calculate_right_boundary(arr, stack, rb):

    for i in range(len(arr)-1, -1, -1):
        if len(stack) ==0:
            rb.append(len(arr))
            stack.append(i)
        else:
            if arr[i]<arr[stack[-1]]:
                # not ideal condition, find smaller ele by popping until found
                while(len(stack)>0 and arr[i]<arr[stack[-1]]):
                    # pop bade elements
                    stack = stack[0:-1]
                if len(stack) ==0:
                    rb.append(len(arr))
                    stack.append(i)
                else:
                    rb.append(stack[-1])
                    stack.append(i)
            else:
                rb.append(stack[-1])
                stack.append(i)
    return rb

def calculate_left_boundary(arr, stack, lb):

    for i in range(0, len(arr)):
        if len(stack) ==0:
            lb.append(-1)
            stack.append(i)
        else:
            if arr[i]>arr[stack[-1]]:
                # ideal condition
                lb.append(stack[-1])
                stack.append(i)
            else:
                # arr[i]<=arr[stack[-1]]: not ideal conditoon, badon ko pop, until found
                while(len(stack)>0 and arr[i]<=arr[stack[-1]] ):
                    # pop
                    stack = stack[0:-1]
                # conditions of coming out of loop
                if len(stack) ==0:
                    lb.append(-1)
                    stack.append(i)
                else:
                    lb.append(stack[-1])
                    stack.append(i)

    return lb

main()
