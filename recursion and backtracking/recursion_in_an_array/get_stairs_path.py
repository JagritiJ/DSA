def total_paths(n):
    if n == 0:
        bres = list()
        bres.append("")
        return bres
    if n <= 0:
        bres = list()
        return bres

    paths_1 = total_paths(n - 1)
    paths_2 = total_paths(n - 2)
    paths_3 = total_paths(n - 3)

    complete_paths = list()
    for path in paths_1:
        complete_paths.append("1" + path)
    for path in paths_2:
        complete_paths.append("2" + path)
    for path in paths_3:
        complete_paths.append("3" + path)

    return complete_paths


def main():
    n = int(input())
    result = total_paths(n)
    print(result)


main()