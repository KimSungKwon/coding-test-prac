'''
크루스칼 알고리즘으로 최소비용 신장트리 생성
그 후 가장 값이 큰 간선을 제거하여 신장트리를 두개로 분리
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

n, m = map(int, input().split())

parents = [0] * (n+1)
for i in range(n+1):
    parents[i] = i

edges = []
last = 0    # 가장 마지막에 추가된 간선(가장 비용이 큰 간선)
result = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parents, a) != find_parent(parents, b):
        union_parent(parents, a, b)
        result += cost
        last = cost

print(result - last)
