
from queue import PriorityQueue



q = PriorityQueue()
arr = [3, 15, 9, 33, 24, 78, 80, -12, 56]

# find 3rd largest item using PQ

for i in range(0, len(arr)):
    q.put(arr[i])


for i in range(0, len(arr)-3):
    print(q.get())
       
    
# now the queue has left with 3 elements only
print("3rd largest is ", q.get() )
