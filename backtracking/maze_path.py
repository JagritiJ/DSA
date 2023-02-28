# https://www.geeksforgeeks.org/rat-in-a-maze-backtracking-2/
def maze_path(sr, sc, er, ec, maze, asf, dirs, dirS):
    if sr==er and sc ==ec:

        return 1
    count=0

    for d in range(0, len(dirs)):
        r = sr+dirs[d][0]
        c = sc+dirs[d][1]
        if r>=0 and c>=0 and r<=er and c<=ec and maze[r][c] ==1:
            count+= maze_path(r, c, er, ec, maze, asf+dirS[d], dirs, dirS)

    return asf

def main():
    maze = [[1,0,0,0],
            [1,1,0,1],
            [0,1,0,0],
            [1,1,1,1]
            ]
    n =rows=cols= len(maze)
    sr =sc =0

    er=ec=n-1
    dirS =['h', 'v']
    dirs =[[0, 1],
           [1,0]]
    asf =''
    count = maze_path(sr, sc, er, ec, maze, asf, dirs, dirS)
    print(count)
main()