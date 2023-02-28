# Stacks in python
# Question : https://www.youtube.com/watch?v=4eSFaEOa-l0&list=PL-Jc9J83PIiFj7YSPl2ulcpwy-mwj1SSk&index=104
# from collections import deque
# mystack=deque()

def main():
    mystr = "((a+b)+((c+d)))"
    # mystack = [2,3,4,5,6,7]
    # mystack=mystack[0:-1]
    # print(mystack)
    # mylist = str.split()
    # print(mylist)
    mystack = list()
    # for ch in mystr:   mystack.pop(ch)
# TypeError: 'str' object cannot be interpreted as an integer
    for i in range(0, len(mystr)):
        if mystr[i] == ")":
            # pop until you find opening bracket
            if len(mystack)>0:
                peek = mystack[-1]
                if peek == "(":
                    # there was no content inside, so duplicate brackets
                    print("true")
                    return
                else:
                    while len(mystack)>0:
                        peek = mystack[-1]
                        if peek == "(":
                            mystack=mystack[0:-1]
                            break
                        else:
                            mystack=mystack[0:-1]
                               
        else:
            mystack.append(mystr[i])
    # reached the end of list and didn't find duplicate brackets
    print("false")
    
# if I just append all the chars - print(mystack)
# ['(', '(', 'a', '+', 'b', ')', '+', '(', '(', 'c', '+', 'd', ')', ')', ')']
        
# Test case: (a+b)+(c+d), ((a+b)+((c+d)))  

main()