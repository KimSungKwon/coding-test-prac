'''
크루스칼 알고리즘:
최소 신장 트리 찾기(만들기)

모든 간선들의 비용을 정렬하여 비용이 적은 것부터 간선을 추가. (사이클이 안 생기게: 같은 소속이 아닌 거만)
'''

def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# v: 노드의 개수 e: 간선(union 연산)의 개수
v, e = map(int, input().split())

# 부모 테이블 초기화
parents = [0] * (v+1)
for i in range(v+1):
    parents[i] = i

# 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0
    
# 사용자로부터 union연산 또는 find연산 입력받음
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    # a와 b가 같은 소속이 아니면 연결
    if find_parent(parents, a) != find_parent(parents, b):
        union_parent(parents, a, b)
        result += cost

print(result)
