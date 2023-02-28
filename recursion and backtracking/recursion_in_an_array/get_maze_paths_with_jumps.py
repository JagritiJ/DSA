# This question is the combination of maze path and stair paths questions

def get_maze_paths(sr, sc, dr, dc):

    if sr==dr and sc==dc:
        bres =list()
        bres.append("")
        return bres

    if sr<dr and sc<dc:

        v_paths1 = list()
        v_paths2 = list()
        v_paths3 = list()

        h_paths1 = list()
        h_paths2 = list()
        h_paths3 = list()

        d_paths1 = list()
        d_paths2 = list()
        d_paths3 = list()

        if sr < dr:
            v_paths1 = get_maze_paths(sr + 1, sc, dr, dc)
            v_paths2 = get_maze_paths(sr + 2, sc, dr, dc)
            v_paths3 = get_maze_paths(sr + 3, sc, dr, dc)
        if sc < dc:
            h_paths1 = get_maze_paths(sr, sc+1, dr, dc)
            h_paths2 = get_maze_paths(sr, sc+2, dr, dc)
            h_paths3 = get_maze_paths(sr, sc+3, dr, dc)
        if sr < dr and sc <dc:
            d_paths1 = get_maze_paths(sr+1, sc+1, dr, dc)
            d_paths2 = get_maze_paths(sr+2, sc+2, dr, dc)
            d_paths3 = get_maze_paths(sr+3, sc+3, dr, dc)

        my_paths = list()

        for path in v_paths1:
            my_paths.append("v1"+path)
        for path in v_paths2:
            my_paths.append("v2"+path)
        for path in v_paths3:
            my_paths.append("v3"+path)

        for path in h_paths1:
            my_paths.append("h1"+path)
        for path in h_paths2:
            my_paths.append("h2"+path)
        for path in h_paths3:
            my_paths.append("h3"+path)

        for path in d_paths1:
            my_paths.append("d1"+path)
        for path in d_paths2:
            my_paths.append("d2"+path)
        for path in d_paths3:
            my_paths.append("d3"+path)

        return my_paths

def main():
    m = int(input())
    n = int(input())

    results = get_maze_paths(1, 1, m, n)
    print(results)
main()
