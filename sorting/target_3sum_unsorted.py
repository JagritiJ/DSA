# Given an unsorted list, find pairs with target sum

def find_pairs(arr, target):
    arr.sort()
    l =0
    r = len(arr) -1
    while l<r:
        if arr[l]+arr[r] == target:
            print(arr[l], arr[r])
            l+=1
            r-=1
        elif arr[l]+arr[r]> target:
            r-=1
        else:
            l+=1

def main():
    arr =[20, 40, -30, 10, 50, 80, -77, 90]
    target = 60
    find_pairs(arr, target)

main()