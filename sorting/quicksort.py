# Algorithm for Quicksort
# This algorithm uses 3 pointers - 1 pivot and 2 pointers

def swap(arr, i, j):
    temp = arr[i]
    arr[i]=arr[j]
    arr[j] = temp

def pivoting(arr, si, ei, pivot):
    ptr =si-1
    itr = si

    while(itr<=ei):
        if arr[itr] == arr[ei]:
            swap(arr, pivot, ptr)
        itr+=1
        ptr+=1
    # elif arr[pivot] > arr[itr]:
    #     swap(arr, itr, ptr)

    return pivot

def quicksort(arr,si, ei):
    if si >= ei:
        return

    pivot = ei
    pivot = pivoting(arr, si, ei, pivot)
    quicksort(arr, si, pivot-1)
    quicksort(arr, pivot+1, ei)


def main():
    arr = [20, -60, 68, 0, 8, -7, -35, 40, -59]
    quicksort(arr, 0, len(arr)-1)
    print(arr)

main()
