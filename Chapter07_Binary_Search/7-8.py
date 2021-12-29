n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))

def binary_search(arr, target, start, end):

    while start <= end:
        total = 0
        mid = (start + end) // 2
        
        # 떡들을 mid 높이의 절단기로 잘라서 잘린 떡을 total에 합함
        for i in range(len(arr)):
            temp = arr[i] - mid
            if temp > 0:
                total += temp
        
        # total이 target보다 클 경우: 절단기의 높이를 높임. 낮을 경우: 높이를 낮춤
        if total == target:
            return mid
        elif total >= target:
            start = mid + 1
        else:
            end = mid - 1

    return None

print(binary_search(arr, m, 0, max(arr)))
