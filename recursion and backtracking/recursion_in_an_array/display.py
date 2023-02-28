def main():
    arr = list(map(int, input().split()))
    idx = 0
    display(arr, idx)

def display(arr, idx):
    if idx ==len(arr):
        return
    print(arr[idx])
    display(arr, idx+1)

main()