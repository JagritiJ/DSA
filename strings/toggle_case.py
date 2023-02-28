def toggle_case(mystr):
    newstr = ''
    for ch in mystr:
        if ch == ch.upper():
            newstr += ch.lower()
        else:
          newstr += ch.upper()
    print(newstr)


def main():
    mystr = input()
    toggle_case(mystr)


main()


