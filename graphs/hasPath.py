# doesn't work
class Edge:
  def __init__(self, src, nbr, wt):
    self.src = src
    self.nbr = nbr
    self.wt = wt

def display(self, my_dict):

    size = len(my_dict)
    print(size)
    print(my_dict[0])    

    print("key wise")
    for key in self.my_dict:
        print(self.my_dict[key])

def main():
    vtces = int(input())
    edges = int(input())
    graph = {}
    for i in range(vtces) :
        graph[i] = []

    for i in range(edges) :
        values = input().split(" ")
        v1 = int(values[0])
        v2 = int(values[1])
        wt = int(values[2])
        e1 = Edge(v1, v2, wt)
        e2 = Edge(v2, v1, wt)
        graph[e1.src].append(e1)
        graph[e2.src].append(e2)

    display(graph)
        # src = int(input())
        # dest = int(input())
    # write your code here
    visited =[]
    # result = has_path(graph, src, dest, visited)
    # print(result)

def has_path(graph, src, dest, visited):
    
    if src == dest:
        return True
    
    visited.append(src)
    
    for i in graph[src]:
        nbr = graph[src][1]
        if nbr not in visited:
            has_path(graph, nbr, dest, visited )
            
            if has_path:
                return True
                
    return False
def display(my_dict):

    size = len(my_dict)
    print(size)
    print(my_dict[0])    

    print("key wise")
    for key in my_dict:
        print(my_dict[key])

if __name__ == "__main__":
    main()