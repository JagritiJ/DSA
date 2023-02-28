def main():
    n = int(input())
    m = int(input())
    arr = []

    for i in range(n) :
        values = list(map(int, input().split(" ")))
        arr.append(values)

#write your code here
    visited =[[False for j in range(m)] for i in range(n)]
    count =0
    for i in range(n):
        for j in range(m):
            if arr[i][j] ==0 and visited[i][j]==False:
            # go and check it's neighbours
                dfs(arr, visited, i, j)
                count+=1
  
    print(count)


def dfs(matrix, visited, i, j):

    if i <0 or i >=len(matrix) or j <0 or j >= len(matrix[0]) or matrix[i][j] ==1 or visited[i][j]==True:
        return
  
    visited[i][j] =True
  
    dfs(matrix, visited, i-1, j)
    dfs(matrix, visited, i+1, j)
    dfs(matrix, visited, i, j-1)
    dfs(matrix, visited, i, j+1)

main()