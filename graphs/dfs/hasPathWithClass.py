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
  dest = int(input())
  visited = [0]*verts

  print("true") if(haspath(graph,src, dest, visited)) else print("false")
  
def haspath(graph, src, dest, visited):
  if(src == dest):
    return True
  visited[src] = 1
  
  for edge in graph[src]:
    # Remember edge is a class, so if I print out that, I will only get an object's address
    # Now, to get the value, access the attributes of the class usin g the object.attribute syntax
    # print("edge.nbr is ", edge.nbr)
    if(visited[edge.nbr] ==0):
      p = haspath(graph, edge.nbr, dest, visited)
      if(p==True):
        return True
        
  return False
      
    
if __name__== "__main__":
  main()