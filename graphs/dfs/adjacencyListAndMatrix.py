# without class

def main():

    verts= 4
    edges = [[0,1], [0,2], [0,3], [1, 2], [3,2]]

    # adjaList(verts, edges)
    adjaMatrix(verts, edges)

def adjaList(verts, edges):

    # initialize the graph
    my_dict = {my_list: [] for my_list in range(verts)}
    for v1, v2 in edges:
        my_dict[v1].append(v2)

    print(str(my_dict))
    display(my_dict)

def display(my_dict):

    size = len(my_dict)
    print(size)
    print(my_dict[0])    

    print("key wise")
    for key in my_dict:
        print(my_dict[key])

def adjaMatrix(verts, edges):

    # initialize the graph
    matrix = [[0 for j in range(verts)] for i in range( verts)]
    print(matrix)
    for v1, v2 in edges:
        matrix[v1][v2]=1

    print(str(matrix))

    for i in range(verts):
        for j in range (verts):
            print(matrix[i][j])
   


if __name__ == "__main__":
    main()