'''
섬 연결하기
https://programmers.co.kr/learn/courses/30/lessons/42861

kruskal 알고리즘 사용
'''
def solution(n, costs):
    answer = 0
    costs.sort(key= lambda x: x[2])
    accessible = set([costs[0][0], costs[0][1]])
    answer += costs[0][2]

    while len(accessible) < n:
        for cost in costs[1:]:
            if cost[0] in accessible and cost[1] in accessible:
                continue
            if cost[0] in accessible or cost[1] in accessible:
                accessible.update([cost[0], cost[1]])
                answer += cost[2]
                break


    return answer
