# https://www.youtube.com/watch?v=4bjCEJmiPZA&list=PL-Jc9J83PIiEyUGT3S8zPdTMYojwZPLUM&index=44
# along with all the operations of the stack, you should be able to get the min in O(1) 
# this will require 2 stacks, allData and minData

class Stack:  
    # Constructor - parameterized  

    data = []
    length = 0
    value = None
    def __init__(self, ):
        pass
        # print("This is parametrized constructor")  
        # self.length = length
        # self.data = [0]*self.length
        

    def size(self):  
        print("No. of members is", self.length)
        return self.length  
    
    def push(self, val):
        # very tricky, in a way you need to push all the elements by 1 to accomodate the latest element
        # if len(self.data)>self.length:
        #     print("Stack Overflow")
        # else:
        self.value = val         
        self.data.append(self.value)

    def pop(self):
        if len(self.data) ==0:
            print("Stack Underflow")
        else:
            self.data = self.data[0:-1]
            self.length = self.length-1
    
    def top(self):
        print("top is ", self.data[-1])
        return self.data[-1]
    
    def display(self):
        for i in range(0, len(self.data)):
            print("Value of ", i, self.data[i])
        
def main():
    # input data received
    data = list(map(int, input().split()))
    length = len(data)
    # declaring 2 stacks (will use list as stack)    
    allData = Stack()
    minData = Stack()

    # insert first item
    allData.push(data[0])
    minData.push(data[0])

    # now there will be comparison
    for i in range(1, len(data)):
        if data[i]<minData.top():
            minData.push(data[i])
        allData.push(data[i])

    allData.display()
    print("min stack after pushing elements")
    minData.display()

    top_allData = allData.top()
    top_minData = minData.top()

    # popping
    # When you need to pop
    # if the value at top of allData == minData, then pop from both stacks. Else just pop from AllData
    for i in range(0, allData.size()):
        if top_allData == top_minData:
            # pop from both
            allData.pop()
            minData.pop()
        else:
            allData.pop()
        
    # allData.display()
    print("min stack")
    minData.display()

main()