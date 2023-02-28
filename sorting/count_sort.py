# implement count sort
# find the range yourself

def count_sort(arr):
    max_num = max(arr)
    freq = [0 for i in range(0, max_num+1 )]
    for i in range(0, len(arr)):
        freq[arr[i]] += 1
    print(freq)

def main():
    arr =[1, 4, 1, 2, 7, 5, 2]
    count_sort(arr)

main()