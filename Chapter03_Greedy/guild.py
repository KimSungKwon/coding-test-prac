'''
Q 01
모험가 길드
'''

n = int(input())  # 불 필요..

data = list(map(int, input().split()))
data.sort(reverse=True) # 그리디를 위해 정렬

group = 0 # 여행을 떠날 수 있는 그룹 수
while data:
    top = data[0]
    if top <= len(data):  # 필요한 모험가의 수가 남아있는 모험가의 수보다 적으면 
        for i in range(top):
            data.pop(0)
        group += 1
    else: # 필요한 모험가의 수가 남아있는 모험가의 수보다 크면
        break

print(group)
