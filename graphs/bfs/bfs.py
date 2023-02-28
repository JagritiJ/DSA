# TLE Error -- check when to write == and =, sometime, usinging == fpor assignment and it's getting into infin ite loop for visited as it's was not updating at all

from queue import Queue

class Edge:
  def __init__(self, src, nbr):
    self.src = src
    self.nbr = nbr

def main():
    vtces = int(input())
    edges = int(input())
    graph = {}
    for i in range(vtces) :
        graph[i] = []

    for i in range(edges) :
        lines = input().split(" ")
        v1 = int(lines[0])
        v2 = int(lines[1])
        e1 = Edge(v1, v2)
        e2 = Edge(v2, v1)
        graph[e1.src].append(e1)
        graph[e2.src].append(e2)

    src = int(input())
    myqueue =Queue()
    visited = [False]*vtces

    myqueue.put(src)
    psf = ""
    while (myqueue.empty()==False):
        vertex = myqueue.get()
        psf+=str(vertex)
        # myqueue[1:]
       
        if visited[vertex] ==True:
            print("Cycle ", psf)
            continue

        visited[vertex] =True
        print(vertex, end="")
        for edge in graph[vertex]:
            if visited[edge.nbr] ==False:
                myqueue.put(edge.nbr)

    # print(psf)

#write your code here

if __name__ == "__main__":
    main()
