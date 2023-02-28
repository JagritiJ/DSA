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
  
  print(components)

def get_connected_comps(graph, verts, visited, comps):

    for src in range(0, verts):
        comp =[]
        component = drawTree(graph, src, visited, comp)
        comps.append(component)
            
    return comps

def drawTree(graph, src, visited, comp):
    visited[src] = 1
    comp.append(src)
    
    for edge in graph[src]:
        # Remember edge is a class, so if I print out that, I will only get an object's address
        # Now, to get the value, access the attributes of the class usin g the object.attribute syntax
        # print("edge.nbr is ", edge.nbr)
        if(visited[edge.nbr] ==0):
            comp.append(edge.nbr)
            get_connected_comps(graph, edge.nbr, visited, comp)
    
    return comp
    
if __name__== "__main__":
  main()