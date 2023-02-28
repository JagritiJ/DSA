from queue import PriorityQueue

arr = [3, 15, 9, 33, 24, 78, 80, -12, 56]

# find a number just larger than 25
just_larger_than = 25

pq = PriorityQueue()
# sort and find the number
# arr.sort()
print(arr)
for i in range(0, len(arr)):
    if arr[i]>just_larger_than:
        # put them in a priority queue
        pq.put(arr[i])    
# without sorting

print(pq.get())