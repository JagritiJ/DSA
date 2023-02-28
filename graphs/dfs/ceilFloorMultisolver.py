from queue import PriorityQueue

class Edge():
  def __init__(self, src, nbr, wt):
    self.src = src
    self.nbr = nbr
    self.wt = wt

def main(): 
    verts = int(input())
    edges = int(input())
    graph = {}
    for i in range(verts):
        graph[i] = []
    
    for i in range(edges):
        a, b, c = map(int, input().split())
        graph[a].append(Edge(a, b, c))
        graph[b].append(Edge(b, a, c))  
    
    src = int(input())
    dest = int(input())
    criteria = int(input())
    k = int(input())
    visited = [0]*verts
    wsf =0

    answers = print_all_paths(graph,src, dest, visited, "0", wsf, criteria, k)     
    print("answers ", answers)
    print("a ", answers[0])
    print("b ", answers[1])
    print("c ", answers[2])
    print("d ", answers[3])

    # for i in range(0, pq.qsize-3):
    #     print(pq.get())
       
    # # now the queue has left with 3 elements only
    # print("3rd largest is ", pq.get() )
smallest_wt = float('inf')
largest_wt = float('-inf')
ceil_wt = float('inf')
floor_wt = float("-inf")
pq = PriorityQueue()  

def print_all_paths(graph, src, dest, visited, psf, wsf,  criteria, k):
    global smallest_wt, largest_wt, ceil_wt, floor_wt, pq
    if(src == dest):
        # find smallest path
        if wsf <smallest_wt:
            smallest_wt =wsf
            # print(psf)
        
        # find largest path
        if wsf >largest_wt:
            largest_wt = wsf
            # print(psf)

        # Ciel is - just larger than criteria, or largest values me se min
        if wsf >criteria and wsf <ceil_wt:
            ceil_wt= wsf
        #    print("Ceil is ", ceil_wt)

        # Ciel is - just larger than criteria, or largest values me se min
        if wsf <criteria and wsf >floor_wt:
            floor_wt= wsf
        #    print("Ceil is ", floor_wt)

        # k largest value requires priority queue
        pq.put(wsf)
        return [smallest_wt, largest_wt, ceil_wt, floor_wt, pq]
    
    visited[src] = 1
    for edge in graph[src]:
        # Remember edge is a class, so if I print out that, I will only get an object's address
        # Now, to get the value, access the attributes of the class usin g the object.attribute syntax
        # print("edge.nbr is ", edge.nbr)
        if(visited[edge.nbr] ==0):
            npsf = psf + str(edge.nbr)
            nwsf = wsf +edge.wt
            print_all_paths(graph, edge.nbr, dest, visited, npsf, nwsf, criteria, k)
    visited[src] =0

if __name__== "__main__":
  main()