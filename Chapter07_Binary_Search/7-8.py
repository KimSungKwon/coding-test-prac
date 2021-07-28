answer = 0

def bs(arr, target, start, end):
    global answer
    
    while start <= end:
        mid = (start+end) // 2
        result = 0

        # 높이가 mid인 절단기로 떡 자르기. 떡의 양 == result
        for e in arr:
            if e > mid:
                result += e - mid
        
        # 최적의 해
        if result == target:
            answer = mid
            break
        # 떡의 양이 모자름 => 절단기의 높이를 줄임
        elif result < target:
            end = mid - 1
        # 떡의 양이 초과됨 => 절단기의 높이를 늘림. 최적의 해 안 나올 수 있으니 일단 결과값 저장
        else:
            answer = mid
            start = mid + 1

n, m = map(int, input().split())
arr1 = list(map(int, input().split()))

arr1.sort()
bs(arr1, m, 0, max(arr1))
print(answer)
