'''
Q43 어두운 길

최소 신장 트리 문제
'''

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n)
edges = []

for i in range(n):
    parent[i] = i

for i in range(m):
    x, y, z = map(int, input().split())
    edges.append((z, x, y))

edges.sort()

result = 0
total = 0
# total: 전체 가로등의 값
# result: 실제로 쓰는 가로등의 값
for edge in edges:
    z, x, y = edge
    total += z
    if find_parent(parent, x) != find_parent(parent, y):
        union(parent, x, y)
        result += z

# total - result: 절약할 수 있는 가로등의 값
print(total - result)
