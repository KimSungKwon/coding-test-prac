'''
위장
https://programmers.co.kr/learn/courses/30/lessons/42578

경우의 수 : (A종류의 의상 수 + 1) * (B종류의 의상 수 + 1) * (C종류의 의상 수 +1) * ...  - 1
만약 A종류의 의상 수가 2개면 A-a입기 or A-b입기 or 안 입기
최소 한 개의 의상을 입어야 하므로 모든 의상을 안 입는 경우의 수 제외
hash = {'의상의 종류': [의상의 이름들 리스트]}
'''

def solution(clothes):
    answer = 1
    dict = {}

    for e in clothes:
        if e[1] in dict.keys():
            dict[e[1]].append(e[0])   # A 
        else:
            dict[e[1]] = [e[0]]   # 최초로 딕셔너리에 삽입할 시 리스트타입으로 삽입. 안 그러면 A에서 오류

    for e in dict:
        answer *= (len(dict[e]) + 1) 

    answer -= 1   # 모든 의상을 안 입는 경우의 수 제외

    return answer
