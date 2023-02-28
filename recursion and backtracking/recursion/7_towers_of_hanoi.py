# https://www.youtube.com/watch?v=uwrc4H3yaJ4&list=PL-Jc9J83PIiFxaBahjslhBD1LiJAV7nKs&index=11

def main():
    # take input for no. of disks
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())

    toh(n, a,b,c)
    # we need to move the disks, from A -> B tower using C tower
def toh(n, A, B, C):
    if n ==0:
        return
    toh(n-1, A, C, B)
    print(n , " ", A, "moved to" , B )
    toh(n-1, C, B, A)

main()