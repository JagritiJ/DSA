# https://www.youtube.com/watch?v=R7qja_gZrvI&list=PL-Jc9J83PIiFxaBahjslhBD1LiJAV7nKs&index=10

def main():
    n = int(input())
    pzz(n)

def pzz(n):
    if n==0:
        return
    print("Pre ", n)
    pzz(n-1)
    print("In ", n)
    pzz(n-1)
    print("Post ", n)

main()

# 2
# Pre  2
# Pre  1
# In  1
# Post  1
# In  2
# Pre  1
# In  1
# Post  1
# Post  2