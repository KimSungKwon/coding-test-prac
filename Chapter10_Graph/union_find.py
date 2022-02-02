'''
함수 구현 부분
'''
def find_parent(parent, x):
    # x가 루트노드가 아니면
    if parent[x] != x:
        return find_parent(parent, parent[x])
    # x가 루트노드면 x 리턴
    return x

def union_parent(parent, a, b):
    # 각각 루트노드 찾기
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    # 루트노드 비교해서 큰 놈의 루트노드를 작은 놈의 루트노드로 변경
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

'''
사용자 입력, 함수 실행 부분
'''
v, e = map(int, input().split())
parents = [0] * (v+1) # 노트번호가 1부터 시작

# 각 노드의 루트노드를 자기 자신으로
for i in range(1, v+1):
    parents[i] = i 

# union 연산 
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parents, a, b)

# 결과값 출력
print('각 원소가 속한 집합: ', end='')
for i in range(1, v+1):
    print(find_parent(parents, i), end=' ')
print()
print('부모 테이블: ', end='')
for i in range(1, v+1):
    print(parents[i], end=' ')
