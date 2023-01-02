'''
큰 수 만들기
https://programmers.co.kr/learn/courses/30/lessons/42883

stack사용. 왼쪽부터 순서대로 숫자를 삽입
삽입하기 전에 stack의 마지막 값이 삽입하려는 값보다 크거나 같을 때까지 pop. k가 0 이하인 경우 그냥 진행
while문을 빠져나가고 k가 1 이상일 경우 k값 만큼 pop
'''

def solution(number, k):
    answer = ''   
    stack = []    # 스택에서 가장 큰 수를 만들어나감

    for element in number:   
        while stack and stack[-1] < element and k != 0:    # 현재 값과 스택의 끝값을 비교해서 넣고 뺌
            stack.pop()
            k -= 1    # 숫자 빼기 하나 소모
        stack.append(element)

    while k > 0:  # k가 남아있을 경우 스택의 가장 큰 수에서 맨 끝부터 뺴감
        stack.pop()
        k -= 1

    answer = "".join(stack)

    return answer
