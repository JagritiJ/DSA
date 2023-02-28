def main():
    x =[1, 2,3,4]
    y =[11, 12, 13, 14]
    #
    # for i, j in zip(x, y):
    #     print(i, j)

    for i, j in zip(range(len(x)), range(9)):
        print(i, j)

main() 