'''
입국심사
https://programmers.co.kr/learn/courses/30/lessons/43238

파라메트릭 서치 방법 (최적 구하기)
'''

def solution(n, times):
    answer = 0
    start = 0
    end = max(times) * n
    
    while start <= end:
        # mid: 모든 사람이 검사받은 시간
        mid = (start + end) // 2
        people = 0
        
        for time in times:
            # people: mid시간동안 총 검사받을 수 있는 사람 수
            people += mid // time
            
        # people이 n과 같음: 시간이 딱 맞음(최적)
        # people이 n보다 큼: 시간이 남아 돔 (더 적게 설정하기), 일단 답으로 설정
        if people >= n:
            answer = mid    
            end = mid - 1
        else:
            start = mid + 1
            
    return answer
