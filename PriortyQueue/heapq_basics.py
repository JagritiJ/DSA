# Priority Queue helps in sorting
# just like queue, also where we can priortise either smallest or largest number, so that goes out first
# when you remove 1 element, the priority queue then gets the next smallest element in the bill, so heapify is done automatoically
# by default smallest is set automatically. but yoy can set largest manually
# add and remove O(log(n)) and peek O(1)
# heapq.heapify(mylist) - makes changes in the heap, so changes internally, don't need a return 
# sorted based on first number in list and also in ascending order

import heapq
import random
random.seed(42)

mylist = [(1, "Andrew"), (3, "Karl"), (5, "Cian"), (2, "Raymond"), (4, "Dave") ]
heapq.heapify(mylist)
print(mylist)

 # myheap = heapq() -- wrong way of creating heap
heap = []
for i in range(10):
    val = random.randint(1,10)
    heapq.heappush(heap, val)

heapq.heappush(mylist, (6, "Ben"))
heapq.heappop(mylist)

print("after popping ", mylist)
heapq.merge(mylist, heap)
# pop smallest and put this item
heapq.heapreplace(mylist, (7, "Nick" ))



# Create sorted sequences

sequence1 = [1,2,3]; # A list

sequence2 = (5,7,9); # A tuple

sequence3 = {6,8,10}; # A set


# Merge the sequences

merged = heapq.merge(sequence1, sequence2, sequence3);

# Print the merged sequences

print("The merged sequence:")
for item in merged:
    print(item)

# nlargest and nsmallest
select = 4

elements = (2, 9, 17, 11, 6, 16, 8)

smallests = heapq.nsmallest(select, elements)
print("Smallests ", smallests)

largests = heapq.nlargest(select, elements)
print("Largests ", largests)

# Couldn't find an inbuilt way of using heapq in descending order