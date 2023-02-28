# wrong answer

from collections import deque

class Edge():
  def __init__(self, src, nbr, weigh):
    self.src = src
    self.nbr = nbr
    self.weigh = weigh
   
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
    visited =[0]*verts

    stack = deque()
    psf =""
    stack.append(src)

    while len(stack) >0:
        item = stack.pop()
        if visited[item]==True:
            continue

        visited[item] =True
        # psf+=str(item)
        print(str(item))
        for edge in graph[src]:
            if visited[edge.nbr] ==False:
                stack.append(edge.nbr)

    # print(psf)



if __name__ == "__main__":
    main()