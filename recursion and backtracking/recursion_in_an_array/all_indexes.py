# https://www.youtube.com/watch?v=5Q5ed7PWJ8I&list=PL-Jc9J83PIiFxaBahjslhBD1LiJAV7nKs

def main():

    arr = [2,3,6,9,8,3,2,6,2,4]
    x = 3
    mylist =[]
    answer = all_indexes(arr, 0, x, mylist)
    print("Answer is ", answer)

def all_indexes(arr, idx, x, mylist):
    if idx == len(arr):
        return
    
    if arr[idx] ==x:
        mylist.append(idx)
    
    all_indexes(arr, idx+1, x, mylist)
    
    return mylist

main()