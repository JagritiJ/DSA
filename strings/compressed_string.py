def compress_string(mystring):
    count = 1
    new_str = mystring[0]
    for ch in range(1, len(mystring)):
        if mystring[ch] == mystring[ch - 1]:
            count += 1
            continue
        else:
            new_str= new_str+mystring[ch]
        # if count > 1:
        #     print(mystring[ch-1]+str(count), end="")
        # else:
        #     print(mystring[ch-1], end="")
        # count = 0
    print(new_str)

def main():
    mystring = input()
    compress_string(mystring)


main()