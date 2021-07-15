'''
가장 큰 수
https://programmers.co.kr/learn/courses/30/lessons/42746?language=python3

입력값의 최대값이 1000이하 이므로 *3을 해서 같은 조건으로 세자리 수까지 비교해야 함
모든 원소가 0일 때, "0000"이 아닌 '0' 출력해야 함
'''

def solution(numbers):
    answer = ''
    
    numbers = list(map(str, numbers))
    numbers.sort(key= lambda x: x*3, reverse=True)

    for i in range(len(numbers)):
        answer += numbers[i]
    
    if numbers[0] == '0':  # if numbers is [0, 0, 0, 0], return '0' not "0000"
        return '0'

    return answer
