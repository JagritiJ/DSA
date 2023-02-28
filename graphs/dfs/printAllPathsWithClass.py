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

  print_all_paths(graph,src, dest, visited, "0")
  
def print_all_paths(graph, src, dest, visited, psf):
  if(src == dest):
    print(psf)
    return 
  
  visited[src] = 1
  for edge in graph[src]:
    # Remember edge is a class, so if I print out that, I will only get an object's address
    # Now, to get the value, access the attributes of the class usin g the object.attribute syntax
    # print("edge.nbr is ", edge.nbr)
    if(visited[edge.nbr] ==0):
      npsf = psf + str(edge.nbr)
      print_all_paths(graph, edge.nbr, dest, visited, npsf)
  visited[src] =0

if __name__== "__main__":
  main()