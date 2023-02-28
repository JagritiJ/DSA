def reverse_list(mylist):

    # return mylist[::-1] -- does not work for lists
    for i in range(int(len(mylist)/ 2)):
        j = len(mylist)-1-i
        # swap(mylist[i], mylist[j])
        temp = mylist[i]
        mylist[i] = mylist[j]
        mylist[j] = temp
    return mylist

def reverse_string():

    str = "abcd"
    # this -1 logic works only in strings
    print(str[::-1])

def swap(i, j):
    temp = i
    i = j
    j = temp

if __name__ == "__main__":

    n = int(input())
    mylist = [int(input()) for i in range(n)]
    result = reverse_list(mylist)

    # print(result)
    for i in range(len(result)):
        print(mylist[i], end=" ")

    reverse_string()