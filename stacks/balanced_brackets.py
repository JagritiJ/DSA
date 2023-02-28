# Q; https://www.youtube.com/watch?v=p-RbQyQevTQ&list=PL-Jc9J83PIiEyUGT3S8zPdTMYojwZPLUM&index=4
# Test Cases: [(a+b)+{(c+d)*(e/f)}] -- balanced
# [(a+b)+{(c+d)*(e/f)]} -- not balanced, mismatch of closing brackets
# opening brackets more, closing brackets more

def main():
    mystr = input()
    mystack=list()
    for i in range (0, len(mystr)):
        if mystr[i] == "(" or mystr[i] == "{" or mystr[i] == "[":
            mystack.append(mystr[i])
        elif mystr[i] ==")":
            # pop until found ")"
            val, mystack = handleClosing(mystack, "(")
            if val ==False:
                print(val)
                return
            

        elif mystr[i] =="}":
            val, mystack = handleClosing(mystack, "{")
            if val ==False:
                print(val)
                return
        elif mystr[i] =="]":
            val, mystack = handleClosing(mystack, "[")
            if val ==False:
                print(val)
                return        
        else:
            print("do nothing")
    if len(mystack)==0:
        print("true")       

def handleClosing(mystack, ch):
    top = mystack[-1]
    if len(mystack)==0:
        return [False, mystack]
    elif mystack[-1] != ch:
        return [False, mystack]
    else:
        mystack = mystack[0:-1]
        return [True, mystack]

main()

# [(a+b)+{(c+d)*(e/f)}]
# do nothing
# do nothing
# do nothing
# do nothing
# do nothing
# do nothing
# do nothing
# do nothing
# do nothing
# do nothing
# do nothing
# true

# Second test case:
# [(a+b)+{(c+d)*(e/f)]}
# do nothing
# do nothing
# do nothing
# do nothing
# do nothing
# do nothing
# do nothing
# do nothing
# do nothing
# do nothing
# do nothing
# False