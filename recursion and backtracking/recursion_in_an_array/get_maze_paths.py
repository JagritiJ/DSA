# def get_maze_paths(m, n):
#
#     if m<0 or n<0:
#         bres = list()
#         return bres
#     elif m==0 or n==0:
#         bres =list()
#         bres.append("")
#         return bres
#
#     m_paths = get_maze_paths(m-1, n)
#     n_paths = get_maze_paths(m, n-1)
#
#     my_paths = list()
#     for path in m_paths:
#         my_paths.append("v"+path)
#     for path in n_paths:
#         my_paths.append("h"+path)
#
#     return my_paths

def get_maze_paths(sr, sc, dr, dc):

    if sr==dr and sc==dc:
        bres =list()
        bres.append("")
        return bres
    v_paths = list()
    h_paths = list()
    if sr<dr:
        v_paths = get_maze_paths(sr+1,sc, dr, dc)
    if sc<dc:
        h_paths = get_maze_paths(sr,sc+1, dr, dc)

    my_paths = list()
    for path in v_paths:
        my_paths.append("v"+path)
    for path in h_paths:
        my_paths.append("h"+path)

    return my_paths


def main():
    m = int(input())
    n = int(input())

    results = get_maze_paths(1,1, m, n)
    print(results)
main()
