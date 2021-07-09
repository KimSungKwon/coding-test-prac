'''
주식가격
https://programmers.co.kr/learn/courses/30/lessons/42584?language=python3

O(n^2)
'''

def solution(prices):
    answer = []
    length = len(prices) - 1

    for i in range(length):
        temp = 1
        for j in range(i + 1, length):
            if prices[i] <= prices[j]:
              temp += 1
            else:
              break
        answer.append(temp)
    
    answer.append(0)

    return answer
