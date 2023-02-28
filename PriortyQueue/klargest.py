# implement klragest on your own
import heapq

def main():
    # 1. Create a priority Queue of k size, here we need kargest value. 
    # At heapq we can have only smallest value at peek
    # 2. Then you can pop smallest value out from k sized priority queue.
    # 3. At the end you will be left k largest values 
    
    # Take Input 
    mylist = list(map(int, input().split()))
    k = int(input())
   
    heapq.heapify(mylist)
    print("After heapifying the list ", mylist)
    # [-4, 1, 8, 2, 6, 16, 17, 11, 2, 9] -- might look like it's sorted. But actually remember this is a heap.
    # Maybe check the popping activity and you will see the pop happens correctly
    # 10-1-7 = 7 is not closed boundary, so basically loop will go on for 9, 8, 7
    for i in range(len(mylist)-1, k-1, -1):
        heapq.heappop(mylist)
    
    print("After popping from the heap ", mylist)

    # 2 9 17 11 6 16 8 1 2 -4

def klargest():
    pass

main()

