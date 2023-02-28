# without class

def main():

    verts= 4
    edges = [[0,1], [0,2], [0,3], [1, 2], [3,2]]
    src = int(input())
    dest = int(input())
    
    graph = adjaList(verts, edges)
    visited =[]
    result = has_path(graph, src, dest, visited)  
    print(result)

def adjaList(verts, edges):

    # initialize the graph
    my_dict = {my_list: [] for my_list in range(verts)}
    for v1, v2 in edges:
        my_dict[v1].append(v2)

    # print(str(my_dict))
    # display(my_dict)
    return my_dict
   
def display(my_dict):

    size = len(my_dict)
    print(size)
    print(my_dict[0])    

    print("key wise")
    for key in my_dict:
        print(my_dict[key])

def has_path(graph, src, dest, visited):
    if src == dest:
        return True
    
    visited.append(src)
    for nbr in graph[src]:
        if nbr not in visited:
            has_path(graph, nbr, dest, visited)

    return False

if __name__ == "__main__":
    main()