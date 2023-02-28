# This is not working correctly
# write a program to implement a stack
#  stack - add elemets at top and remove from top.
# Methods to implement - push, pop, top, size
# check what are the given information, n = no. of elements to be put in stack

# class Family:  
#     # Constructor - parameterized  
#     members=5
#     def __init__(self, count):  
#         print("This is parametrized constructor")  
#         self.members = count
#     def show(self):  
#         print("No. of members is", self.members)  
        
# object = Family(10)  
# object.show()  

class Stack:

    # def Stack(n):
    #     pass
    n =0
    val = 0
    data = []

    def __init__(self, n, val):
        # create a list/arr of size n
        self.n = n
        self.val= val
        self.data = [0]*(self.n)

    def push(self, val):
        # added at the top
        if len(self.data)>self.n:
            print("Stack Overflow")
            return -1
        else:
            self.data.append(val)
            return self.data

    def pop(self):
        if len(self.data) <=0:
            print("Stack Underflow")
            return -1
        else:
            self.data = self.data[0:-1]
            return self.data
    
    def top(self):
        if len(self.data) <=0:
            print("Stack Underflow")
            return -1
        else:
            tos = self.data[-1]
            return tos

    def size(self):
        return len(self.data)

    def display(self):
        for i in range(0, len(self.data)):
            print(self.data[i])

def main():
    # getting input for the size of stack

    n = int(input())
    stack1 = Stack(n, 0)
    stack1.display()
    stack1 = stack1.push(10)
    print(stack1)
    tos = stack1.top()
    print("tos ", tos)

    # size = stack1.size()
    # print("size is ", size)
    # stack1 = stack1.push(20)
    # stack1 = stack1.push(30)
    # stack1 = stack1.pop()
    # stack1 = stack1.push(40)
    # tos = stack1.tos()

main()