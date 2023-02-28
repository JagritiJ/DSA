# https://www.youtube.com/watch?v=iHM1FPLGcsU&list=PL-Jc9J83PIiEyUGT3S8zPdTMYojwZPLUM&index=19

def main():
    n = input()
    people = list()
    for i in range(0, n):
        people.append(i)

    # initialize an 2d list called arr
    rows, cols = (5, 5)
    arr = [[0]*cols]*rows
   
    # fill the arr, but need to take input line by line
    for i in range(0,n):
        line = input()
        for j in range(0, n):
            arr[i][j] = int(line[j])

    # Create a temp stack and fill it with all the people
    stack = list()
    for i in range(0, n):
        stack.append(i)
    
    # take 2 ppl out of stack for comparison
    i = stack[-1]
    stack = stack[0:-1]
    j = stack [-1]
    stack = stack[0:-1]

    for k in range(0, n):
        if arr[i][j] ==1:
            # atleast k is not the celebrity, so push it back to stack. Considering, rows - > i knows whom  and j represented "is knwoen by"
            stack.append(i)
        else:
            stack.append(j)
    
    # now there will be only 1 person left in stack and rest all others have been elimiated using the process earlier.
    prospective_celebrity = stack[-1]
   
    # so, now we can check the row and column for this person

    for i in range(0, n):
        if i == prospective_celebrity:
            # skip this value
            print()
        if arr[prospective_celebrity][i] !=0:
            print("no one is a celebrity")
            return -1
    
    for i in range(0, n):
        if i == prospective_celebrity:
            # skip this value
            print()
        if arr[i][prospective_celebrity] !=0:
            print("no one is a celebrity")
            return -1
    
    celebrity = prospective_celebrity
    print("celebrity ", celebrity)

main()