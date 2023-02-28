def substrings(mystring):
    lptr = 0
    rptr = len(mystring)
    for lptr in range(0, len(mystring)):
        for rptr in range(lptr + 1, len(mystring)):
            substring = mystring[lptr:rptr + 1]
            # print(substring)
            if is_palindrome(substring):
                print(substring)


def is_palindrome(substring):
    left = 0
    right = len(substring) - 1

    while left <= right:
        if substring[left] == substring[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


def main():
    mystring = input()
    substrings(mystring)


main()