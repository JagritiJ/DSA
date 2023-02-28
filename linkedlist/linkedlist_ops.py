# First we will define a class called Node and then we make linkedlist
class Node:

    def __init__(self, data):

        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        print(self.head)

def traverse(llist):
    # traverse the linkedlist
    curr = llist.head
    while curr.next != None:
        print(curr.data)
        curr = curr.next


def main():

    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)

     # pointers

    llist.head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth

    traverse(llist)

main()

