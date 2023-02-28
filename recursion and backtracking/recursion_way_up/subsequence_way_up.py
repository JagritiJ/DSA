# this recursion technqiue, we will not store the stach results completely, rather we will use print statements to keep printing after a in cycle

def print_subsequence_way_up(ques, ans):

    if len(ques) == 0:
        print(ans)
        return ""

    ch = ques[0]
    roq = ques[1:]

    print_subsequence_way_up(roq, ""+ans)
    print_subsequence_way_up(roq, ch+ans )
    return

def main():
    str = input()
    print_subsequence_way_up(str, "")
main()