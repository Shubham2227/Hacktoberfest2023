import sys
def CoinDeterminer(arr):
    n = len(arr)
    for i in range(n):
        arr[i] += n*(arr[arr[i]])
        print(arr[i])
    for i in range(n):
        arr[i] = arr[i]//n
    return arr
arr = [4,0,2,1,3]

min_groups = CoinDeterminer(arr)
print(min_groups)
