def fun(a,b):
    if (a>1 or b>1):
        return fun(0,0)+fun(0,1)+fun(a-1, b-1)
    else:
        a=a+1
        b=b-1
    return a+2-b
print(fun(3,3))