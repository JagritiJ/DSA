class Stack:  
    # Constructor - parameterized  
    members=5
    data = []
    length = 0
    value = None
    def __init__(self, length):  
        print("This is parametrized constructor")  
        self.length = length
        # self.data = [0]*self.length
        

    def size(self):  
        print("No. of members is", self.length)  
    
    def push(self, val):
        # very tricky, in a way you need to push all the elements by 1 to accomodate the latest element
        if len(self.data)>self.length:
            print("Stack Overflow")
            
        else:
            self.value = val
            self.data.append(self.value)

    def pop(self):
        self.data = self.data[0:-1]
        self.length = self.length-1
    
    def top(self):
        print("top is ", self.data[-1])
    
    def display(self):
        for i in range(0, len(self.data)):
            print("Value of ", i, self.data[i])
        
object = Stack(4)  
object.size()
object.push(10)
object.push(20)
object.push(30)
object.push(40)
object.push(50)
object.display()
object.top()
object.pop()
object.size()
object.display()


# 0
# 0
# 0
# 0
# 0
# 0
# 0
# 0
# 0
# 0
# 10
# 20
# 30