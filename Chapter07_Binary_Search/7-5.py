import sys

def bin_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif mid < target:
            start = mid + 1
        else:
            end = mid - 1
    return False

# readline()이 input()보다 저렴해서 
n = int(input())
arr1 = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(input())
arr2 = list(map(int, sys.stdin.readline().rstrip().split()))

# sorting for binary search
arr1.sort()

for i in range(m):
    if arr2[i] > arr1[-1] or arr2[i] < arr1[0]:
        False
    if bin_search(arr1, arr2[i], 0, n-1):
        print("yes")
    else:
        print("no")
