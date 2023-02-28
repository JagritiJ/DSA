# Programs on arrays
import sys

def find_max(mylist):
    my_max = -sys.maxsize -1
    for num in mylist:
        my_max = max(my_max, num)

    return my_max

def find_min(mylist):

    my_min= sys.maxsize
    for num in mylist:
        my_min = min(my_min, num)
    return my_min

def find_data(mylist, data):
    if data in mylist:
#         then find index
        for index in range(0, len(mylist)):
            if data == mylist[index]:
                return index
    else:
        return -1

# def find_second_min(mylist):
#     my_min = sys.maxsize
#     for num in mylist:
#         my_min = min(my_min, num)
#         if num > my_min:


def reverse_list(mylist):
    pass

def inverse_list(mylist):
    pass

def rotate_list(mylist, rotate_last):
    pass


if __name__ == "__main__":
    num_elements = int(input())
    mylist =[]
    for i in range(num_elements):
        mylist.append(int(input()))

    mymax = find_max(mylist)
    mymin = find_min(mylist)
    # second_min = find_second_min(mylist)
    print("Mymax, mymin, second_min are ", mymax, " ", mymin, " ")

    # print("enter the element you want to search ")
    # find_data = int(input())
    # find_data(mylist, find_data)
    reverse_list(mylist)
    inverse_list(mylist)

    print("enter the element you want to search ")
    rotate_last = int(input())
    rotate_list(mylist, rotate_last)


