def maze_paths(sr, sc, dr, dc, path):
    if sr > dr or sc > dc:
        return

    if sr == dr and sc == dc:
        print(path)
        return
    if sr < dr:
        maze_paths(sr + 1, sc, dr, dc, path + "h")
    if sc < dc:
        maze_paths(sr, sc + 1, dr, dc, path + "v")


def main():
    m = int(input())
    n = int(input())
    maze_paths(0, 0, m-1, n-1, "")


main()
