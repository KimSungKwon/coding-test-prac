'''
베스트엘범
https://programmers.co.kr/learn/courses/30/lessons/42579

plays_dict: {"장르": 재생횟수 총합}
id_dict: {"장르": [(고유번호, 재생횟수), (A, B), ...]}
plays_sorted: 재생횟수 총합이 높은 순으로 정렬된 리스트

sorted(iterable, key = lambda x : (x[1], -x[0]))  # 튜플의 두번 째 인자를 기준으로 먼저 정렬, 값이 같을 경우 그 다음 첫 번째 인자를 기준으로 역순 정렬
'''

def solution(genres, plays):
    plays_dict = {}
    id_dict = {}
    answer = []

    # 딕셔너리 만듬
    for i in range(len(genres)):
        if (genres[i] in id_dict.keys()):
            id_dict[genres[i]].append((i, plays[i]))
            plays_dict[genres[i]] += plays[i]
        else:
            id_dict[genres[i]] = [(i, plays[i])]
            plays_dict[genres[i]] = plays[i] 
    
    # 재생횟수가 높은 순으로 장르 정렬
    plays_sorted = sorted(plays_dict, key = lambda x : plays_dict[x], reverse = True)

    for element in plays_sorted:
        temp = sorted(id_dict[element], key = lambda x : (x[1], -x[0]), reverse = True)   # 장르에서 재생횟수를 기준(key)으로 내림차순 정렬 (같은 값일 경우 고유번호가 낮은 순으로)
        if(len(temp) < 2):
            answer.append(temp[0][0])
        else:
            answer.append(temp[0][0])
            answer.append(temp[1][0])
    
    return(answer)
