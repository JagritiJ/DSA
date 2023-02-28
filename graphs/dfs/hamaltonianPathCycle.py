# wrong answer, 2/4 test cases failed
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
        e1 = Edge(v1, v2 )
        e2 = Edge(v2, v1 )
        graph[e1.src].append(e1)
        graph[e2.src].append(e2)

    src = int(input())
    visited = [0]*vtces
    osrc = src
    psf = str(src)
    count_visited =0
    hamiltonian_path(graph, src, visited, osrc, psf, count_visited)


# write  your codes here
def hamiltonian_path(graph, src, visited, osrc, psf, count_visited):
    if count_visited == len(graph)-1:
        print(psf, end="")
        # visited[src] =True
        # count_visited +=1-- creating bugs

        for edge in graph[src]:

            if edge.nbr ==osrc:
                print("*")
                break
            else:
                print(".")
                break
        return
        
    
    visited[src] =True
    count_visited +=1
    for edge in graph[src]:
       if visited[edge.nbr] ==False:
            hamiltonian_path(graph, edge.nbr, visited, osrc, psf+str(edge.nbr), count_visited)
    visited[src] =False
if __name__ == "__main__":
    main()