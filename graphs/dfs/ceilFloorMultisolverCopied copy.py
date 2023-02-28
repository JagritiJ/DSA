# import math
# import heapq

# spath = ""
# spathwt = math.inf
# lpath = ""
# lpathwt = -math.inf
# cpath = ""
# cpathwt = math.inf
# fpath = ""
# fpathwt = -math.inf
# h = []

# class Edge:

#   def __init__(self, src, nbr, wt):
#     self.src = src
#     self.nbr = nbr
#     self.wt = wt


# def multisolver(graph, src, dest, visited, criteria, k, psf, wsf):
#   #write your code here

# def main():
#   vtces = int(input())
#   edges = int(input())
#   graph = {}
#   for i in range(vtces) :
#     graph[i] = []

#   for i in range(edges) :
#     values = input().split(" ")
#     e1 = Edge(int(values[0]), int(values[1]), int(values[2]))
#     e2 = Edge(int(values[1]), int(values[0]), int(values[2]))
#     graph[e1.src].append(e1)
#     graph[e2.src].append(e2)

#   src = int(input())
#   dest = int(input())
#   criteria = int(input())
#   k = int(input())

#   visited = [False] * vtces
#   multisolver(graph, src, dest, visited, criteria, k, str(src), 0)
#   print("Smallest Path =", spath + "@" + str(spathwt))
#   print("Largest Path =", lpath + "@" + str(lpathwt))
#   print("Just Larger Path than", criteria, "=", cpath + "@" + str(cpathwt))
#   print("Just Smaller Path than", criteria, "=", fpath + "@" + str(fpathwt))
#   largests = heapq.nlargest(k, h)
#   li = largests[len(largests) - 1]
#   print(str(k) + "th largest path = " + str(li[1]) + "@" + str(li[0]));

#   if __name__ == "__main__":
#     main()