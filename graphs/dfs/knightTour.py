def main():
    n = int(input())
    m = int(input())
    arr = []

    for i in range(n) :
        values = list(map(int, input().split(" ")))
        arr.append(values)
    
    src = input().split(" ")
    i = int(src[0])
    j = int(src[1])

    #write your code here
    visited =[[False for j in range(m)] for i in range(n)]
    psf = str([i,j])
    count =0
    dfs(arr, visited, i, j, psf, count)


def dfs(matrix, visited, i, j, psf):
    if (i <0 or i >=len(matrix) or j <0 or j >= len(matrix[0]) or matrix[i][j] ==1 or visited[i][j]==True):
        if count == len(matrix) * len(matrix[0]):
            print("True")
            return True
  
    visited[i][j] =True
    count+=1
    dfs(matrix, visited, i-2, j+1)
    dfs(matrix, visited, i-1, j+2)
    dfs(matrix, visited, i+1, j+2)
    dfs(matrix, visited, i+2, j+1)
    dfs(matrix, visited, i-2, j-1)
    dfs(matrix, visited, i-1, j-2)
    dfs(matrix, visited, i+1, j-2)
    dfs(matrix, visited, i+2, j-1)

    # for finding all paths, unset 
    visited[i][j] =True

main()