def print_permutations(ques, asf):
    if len(ques) ==0:
        print(asf)
        return
    for i in range(0, len(ques)):
        ch = ques[i]
        lstr =ques[0:i]
        rstr =ques[i+1:]
        print_permutations(lstr+rstr, asf+ch)

def main():
    str = input()
    print_permutations(str, "")
main()
