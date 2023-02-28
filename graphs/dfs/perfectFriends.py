# wrong answer

class Edge():
  def __init__(self, src, nbr):
    self.src = src
    self.nbr = nbr

def main(): 
  verts = int(input())
  edges = int(input())

  graph = {}

  for i in range(verts):
    graph[i] = []
  
  for i in range(edges):
    a, b = map(int, input().split())
    graph[a].append(Edge(a, b))
    graph[b].append(Edge(b, a))  

    visited = [0]*verts
    comps = []
    for i in range(verts):
        comp =[]
        get_connected_comps(graph, i, visited, comp)
        comps.append(comp)
  
    count =0
    for i in range(len(comps)):
        j = i+1
        for j in range(len(comps)):
            count+= len(comps[i]) * len(comps[j])
    return count
  
def get_connected_comps(graph, src,visited, comp):
    visited[src] = True
    comp.append(src)
    for edge in graph[src]:
        if visited[edge.nbr] ==False:
            get_connected_comps(graph, edge.nbr,visited, comp)
    
if __name__== "__main__":
  main()