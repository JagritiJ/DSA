def difference_consecutive_chars(mystr):
    diffstr = ''
    for i in range(1, len(mystr)):
        curr = mystr[i]
        prev = mystr[i - 1]

        diff = ord(curr) - ord(prev)
        diffstr += prev + str(diff)
    diffstr += curr
    print(diffstr)


def main():
    mystr = input()
    difference_consecutive_chars(mystr)


main()
