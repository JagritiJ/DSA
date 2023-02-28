# TLE Error -- check when to write == and =, sometime, usinging == fpor assignment and it's getting into infin ite loop for visited as it's was not updating at all
# why still no correct answer of psf
from queue import Queue

class Edge:
    def __init__(self, src, nbr):
        self.src = src
        self.nbr = nbr

class BFS:
    def __init__(self, vertex, psf):
        self.vertex = vertex
        self.psf = psf

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
    myqueue = Queue()
    visited = [False]*vtces

    myqueue.put(BFS(src, str(src)))

    while (myqueue.empty()==False):
        bfs_ob = myqueue.get()
       
        if visited[bfs_ob.vertex] ==True:
            # print("Cycle ", bfs_ob.psf)
            return True

        visited[bfs_ob.vertex] =True
        print(bfs_ob.vertex, bfs_ob.psf,sep="@")
        for edge in graph[bfs_ob.vertex]:
            if visited[edge.nbr] ==False:
                myqueue.put(BFS(edge.nbr, bfs_ob.psf+str(edge.nbr)))

    return False

if __name__ == "__main__":
    main()


# correct Output:

# 2@2
# 1@21
# 3@23
# 0@210
# 4@234
# 5@2345
# 6@2346

