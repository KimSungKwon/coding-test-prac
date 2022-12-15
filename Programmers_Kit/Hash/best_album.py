'''
베스트엘범
https://programmers.co.kr/learn/courses/30/lessons/42579

gen_play: {"장르": 재생횟수 총합}
gen_id_play: {"장르": [(고유번호, 재생횟수), (A, B), ...]}
gen_play_sort: 재생횟수 총합이 높은 순으로 정렬된 리스트

sorted(iterable, key = lambda x : (x[1], -x[0]))  # 튜플의 두번 째 인자를 기준으로 먼저 정렬, 값이 같을 경우 그 다음 첫 번째 인자를 기준으로 역순 정렬
'''

def solution(genres, plays):
    plays_dict = {}
    gen_id_play = {}
    gen_play_sort = []
    answer = []

    # 딕셔너리 만듬
    for i in range(len(genres)):
        if genres[i] not in gen_play:
            gen_play[genres[i]] = plays[i]
            gen_id_play[genres[i]] = [(i, plays[i])]
            
        elif genres[i] in gen_play:
            gen_play[genres[i]] += plays[i]
            gen_id_play[genres[i]].append((i, plays[i])) 
    
    # 재생횟수가 높은 순으로 장르 정렬
    gen_play_sort = sorted(gen_play, key=lambda x: gen_play[x], reverse=True)
    
    # 장르에서 재생횟수를 기준(key)으로 내림차순 정렬 (같은 값일 경우 고유번호가 낮은 순으로)
    for e in gen_play_sort:
        temp = sorted(gen_id_play[e], key=lambda x: (x[1], -x[0]), reverse=True)
        if (len(temp) < 2):
            answer.append(temp[0][0])
        else:
            answer.append(temp[0][0])
            answer.append(temp[1][0])
    
    return(answer)
