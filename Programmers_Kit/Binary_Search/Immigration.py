'''
입국심사
https://programmers.co.kr/learn/courses/30/lessons/43238

파라메트릭 서치 방법
'''

def solution(n, times):
    answer = 0
    start = 1
    end = max(times) * n

    while start <= end:
        mid = (start+end) // 2
        temp = 0

        # mid 분에 몇 명을 받을 수 있나
        for e in times:
            temp += mid // e  
        
        # mid 분에 더 많은 사람을 받을 수 있으면
        if temp >= n:
            answer = mid
            end = mid - 1
        # 시간이 촉박하면
        else:
            start = mid + 1 

    return answer
