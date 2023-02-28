


def subsequence(str):

    if len(str) ==0:
        bres = set()
        bres.add("")
        return bres

    ichar = str[0]
    ros = str[1:]

    rres = subsequence(ros)

    myset = set()
    for res in rres:
        myset.add(ichar+res)
        myset.add(res)

    return myset

def main():
    # str = "abc"
    str = input()
    result = subsequence(str)
    print(len(result), result)

main()