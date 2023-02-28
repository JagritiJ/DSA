# https://www.youtube.com/watch?v=Zy9XnXw8E7U&list=PL-Jc9J83PIiEyUGT3S8zPdTMYojwZPLUM&index=7
# without using nested for loop
def main():
    input_list= list(map(int, input().split()))
    mystack = list()
    nge = list()
    # initialize nge as we need directly access later indexes
    for i in range(0, len(input_list)):
        # print(i)
        nge.append(None)
    for i in range(len(input_list)-1,-1, -1):
        if len(mystack) ==0:
            nge[i] =-1
            mystack.append(input_list[i])
        else:
            if mystack[-1]>input_list[i]:
                nge[i] = mystack[-1]
                mystack.append(input_list[i])
            else:
                # mystack[-1]<=input_list[i]
                while(len(mystack)>0 and mystack[-1]<=input_list[i] ):
                    # pop the elements until then
                    mystack=mystack[0:-1]    
                
                if len(mystack) ==0:
                    nge[i]=-1
                    mystack.append(input_list[i])
                else:
                    # mystack[-1]>input_list[i]
                    nge[i] = mystack[-1]
                    mystack.append(input_list[i])

    print (nge)

main()

# list
# 0	1	2	3	4	5	6	7	8
# 2	5	9	3	1	12	6	8	7
	
# list
# 0	1	2	3	4	5	6	7	8
# 5	9	12	12	12	-1	8	-1	-1