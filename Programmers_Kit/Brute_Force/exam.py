'''
모의고사
https://programmers.co.kr/learn/courses/30/lessons/42840?language=python3
'''

def solution(answers):
    answer = []
    st_1 = [1, 2, 3, 4, 5]
    st_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    st_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    st_score = [0, 0, 0]

    for i in range(len(answers)):
        if st_1[i % len(st_1)] == answers[i]:
            st_score[0] += 1
        if st_2[i % len(st_2)] == answers[i]:
            st_score[1] += 1
        if st_3[i % len(st_3)] == answers[i]:
            st_score[2] += 1

    maximum = max(st_score)

    for i in range(len(st_score)):
        if maximum == st_score[i]:
            answer.append(i+1)

    return answer
