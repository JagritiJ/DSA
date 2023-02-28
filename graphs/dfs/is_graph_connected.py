# wrong output
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
  
  visited = [0]*verts
  comps =[]
  components = get_connected_comps(graph, verts,visited, comps)
  if components ==1:
     return True
  else:
     return False
  
  # print(components)

def get_connected_comps(graph, verts, visited, comps):

    for src in range(0, verts):
        if visited[src] ==False:
            comp =[]
            drawTree(graph, src, visited, comp)
            comps.append(comp)
            
    return comps

def drawTree(graph, src, visited, comp):
    visited[src] = True
    comp.append(src)
    
    for edge in graph[src]:
        if(visited[edge.nbr] ==False):
            get_connected_comps(graph, edge.nbr, visited, comp)
    
if __name__== "__main__":
  main()