class Edge:
    
    def __init__(self, src, nbr, wt) -> None:
        self.src = src
        self.nbr = nbr
        self.wt = wt
    
    def __str__(self):
        # self.src, self.nbr, self.wt
        return "str"
    
    def __repr__(self):
        # self.src, self.nbr, self.wt
        return str(self.src)+" "+str(self.nbr)+" "+str(self.wt)

def main():

    verts = 4
    # graph =[mylist:[] for mylist in range(verts)]
    graph = {my_list: [] for my_list in range(verts)}
    e1= Edge(0, 3, 40)
    e2 = Edge(0, 1, 20)

    graph[0].append(e1)
    graph[0].append(e2)
    graph[1].append(Edge(1, 3, 40))
    graph[1].append(Edge(1, 2, 40))
    graph[2].append(Edge(2, 3, 40))

    print(graph)
    # print(str(graph[0]))

    # for key in graph:
    #     # print(type(key))
    #     list1 = graph[key]
    #     for val in list1:
    #         print(type(val))

if __name__ == "__main__":
    main()