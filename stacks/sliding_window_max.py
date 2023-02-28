# https://www.youtube.com/watch?v=nKXUyUC3BNA&list=PL-Jc9J83PIiEyUGT3S8zPdTMYojwZPLUM&index=13

def main():
    arr = list(map(int, input().split()))
    k = int(input())

    nge_index = list()
    stack = list()

    nge_index = next_greater_element_index(arr, stack, nge_index)

    j=0
    for i in range(0, len(arr)-k):
        if(j<1):
            j =i
        while nge_index[j] < i+k:
            j = nge_index[j]
        print(arr[j])

def next_greater_element_index(arr, stack, nge_index):
    for i in range( len(arr)-1, -1, -1):
        if len(stack)==0:
            nge_index.append(-1)
            stack.append(i)
        else:
            if arr[i]>arr[stack[-1]]:
                # not ideal condition, we wanted greater element
                while(len(stack)>0 and arr[i]>arr[stack[-1]] ):
                    # pop until bigger element found
                    stack = stack[0:-1]
                if len(stack) ==0:
                    nge_index.append(-1)
                    stack.append(i)
                else:
                    nge_index.append(stack[-1])
                    stack.append(i)
            else:
                nge_index.append(stack[-1])
                stack.append(i)
    return nge_index

main()