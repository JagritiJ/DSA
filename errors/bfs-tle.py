# TLE Error
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
    myqueue =[]
    visited = [0]*vtces

    myqueue.append(src)
    psf = ""
    while len(myqueue)!=0:
        vertex = myqueue[0]
        psf+=str(vertex)
        myqueue[1:]
       
        if visited[vertex] ==False:
            visited[vertex] ==True
            print(vertex)
            for edge in graph[vertex]:
                if visited[edge.nbr] ==False:
                    myqueue.append(edge.nbr)
        else:
            #  if visited[vertex] ==True
            print("Cycle ", psf)
    # print(psf)

#write your code here

if __name__ == "__main__":
    main()
