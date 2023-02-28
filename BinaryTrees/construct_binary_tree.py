# https://www.youtube.com/watch?v=XV1ADVV6FbQ&list=PL-Jc9J83PIiHYxUk8dSu2_G7MR1PaGXN4&index=2
# def greeting(name: str) -> str:
# return 'Hello, {}'.format(name)

class Node():

    def __init__(self, data, left, right):
        self.left = left
        self.right = right
        self.data = data

    def display():
        pass

class Pair():
    def__init__(self, node, state):
        self.node= node
        self.state = state
    

def main():

    arr = [50, 25, 12, None, None, 37, 30,
            None, None, None, 75, 62, None, 
            70, None, None, 87]

    stack = deque()

    pair = Pair(arr[i], 1)
    
    for i in range(0, len(arr)):

        if arr[i] == None:
            stack.pop()
        else:
            peek = stack[-1]
            if peek[1] == 1:
                # left child
                if arr[i] != None:
                    ln = Node(arr[i], None, None)
                    peek.node.left =ln
                    stack.append(ln, 1)
            elif peek[1] ==2:
                # right child
                rn = Node(arr[i], None, None)
                peek.node.right =rn
                stack.append(rn, 2)
             
            else: 
                stack.pop()

            




