"""
올바른 괄호
https://school.programmers.co.kr/learn/courses/30/lessons/12909
굳이 자료구조 쓸 필요 없는 듯
"""

def solution(s):
    answer = True
    open = 0
    close = 0

    if s[0] == ')':
        return False
    
    for i in range(len(s)):
        if s[i] == '(':
            open += 1
        else:
            close += 1
            
        if open < close:
            return False

    if open > close:
        return False
    
    return answer
