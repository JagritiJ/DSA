def staircase_way_up(n, path):
    if n <0:
        return
    if n ==0:
        print(path)
        return

    staircase_way_up(n-1, path + "1")
    staircase_way_up(n-2, path + "2")
    staircase_way_up(n-3, path + "3")

def main():
    n = int(input())
    staircase_way_up(n, "")
main()